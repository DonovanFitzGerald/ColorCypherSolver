import random
from Turn import *
from collections import Counter


testColors = ["R", "G", "B", "Y", "P", "W"]
testColorDict = {"R": 0, "G": 0, "B": 0, "Y": 0, "P": 0, "W": 0}
testCypher = ["R", "G", "Y", "W"]
testCypherLength = 4

def contains_all_elements(arr1, arr2):
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    for element in count2:
        if count2[element] > count1[element]:
            return False
    return True

def CreateCypher(cypherLength,colors):    
    cypher = []
    while len(cypher) < cypherLength:
        i = random.randint(0, 5)
        cypher.append(colors[i])
    return cypher

def Algo1(cypher,colorDict,colors, cypherLength):
    turnCount = 1
    while True:
        guess = []
        for i in range(cypherLength):
            guess.append(random.choice(colors))

        Turn(cypher, guess, colorDict) 
        
        if cypher == guess:
            break
        turnCount += 1
    return turnCount


def Algo2(cypher,colorDict,colors,cypherLength):
    turnCount = 1
    validColors = []
    checkedColors = []
    while turnCount < 1000:
        
        guess = []

        if len(colors) != len(checkedColors):
            while len(guess) < cypherLength:
                guess.append(colors[len(checkedColors)])
        else:
            while len(guess) < cypherLength:
                guess.append(random.choice(validColors))
                
        if cypher == guess:
            break
        turnCount += 1
        result = Turn(cypher, guess, colorDict) 
        
        
        if len(colors) != len(checkedColors):
            checkedColors.append(colors[len(checkedColors)])
            if result[0] > 0:
                validColors.append(colors[len(checkedColors) - 1])

        
    return turnCount


def Algo3(cypher,colorDict,colors,cypherLength):
    turnCount = 1
    validColors = {}
    checkedColors = []
    guessHistory = []
    while turnCount < 1000:
        
        guess = []

        if len(colors) != len(checkedColors):
            while len(guess) < cypherLength:
                guess.append(colors[len(checkedColors)])
        else:
            for key, value in validColors.items():
                guess.extend([key] * value)
                
        while guess in guessHistory:
            random.shuffle(guess)
                
                
        guessHistory.append(guess)
                
        if cypher == guess:
            break
        turnCount += 1
        result = Turn(cypher, guess, colorDict) 
        
        
        if len(colors) != len(checkedColors):
            checkedColors.append(colors[len(checkedColors)])
            if result[0] > 0:
                validColors[colors[len(checkedColors) - 1]] = result[0]

        
    return turnCount

def Algo35(cypher,colorDict,colors,cypherLength):
    turnCount = 1
    validColors = {}
    checkedColors = []
    guessHistory = []
    while turnCount < 1000:
        
        guess = []
        
        if sum(validColors.values()) == cypherLength:
            while len(colors) != len(checkedColors):
                checkedColors.append(colors[len(checkedColors)])

        if len(colors) != len(checkedColors):
            while len(guess) < cypherLength:
                guess.append(colors[len(checkedColors)])
        else:
            for key, value in validColors.items():
                guess.extend([key] * value)
                
        while guess in guessHistory:
            random.shuffle(guess)
                
                
        guessHistory.append(guess)
                
        if cypher == guess:
            break
        turnCount += 1
        result = Turn(cypher, guess, colorDict) 
        
        
        if len(colors) != len(checkedColors):
            checkedColors.append(colors[len(checkedColors)])
            if result[0] > 0:
                validColors[colors[len(checkedColors) - 1]] = result[0]

        
    return turnCount

def Algo45(cypher,colorDict,colors,cypherLength):
    
    turnCount = 1
    guessHistory = []
    validColors = []
    validColorsAmounts = {}
    postitionDict = {}
    checkedColors = []
    
    for i in range(len(colors)):
        validColors.append(colors[i])
    
    while turnCount < 10000: #Start of 4
        
        guess = []
        
        for i in range(cypherLength):
            postitionDict[i] = {}
            for j in range(len(colors)):
                postitionDict[i][colors[j]] = 0.001
                
        if sum(validColorsAmounts.values()) == cypherLength:
                while len(colors) != len(checkedColors):
                    checkedColors.append(colors[len(checkedColors)])
                    
        if len(colors) != len(checkedColors):
                while len(guess) < cypherLength:
                    guess.append(colors[len(checkedColors)])
                
        if len(colors) == len(checkedColors):
            while guess in guessHistory or guess == []:
                guess = []
                
                # for i in range(cypherLength):
                #     guess.append(random.choice(colors))
                
                baseGuess = []
                
                for key, value in validColorsAmounts.items():
                    baseGuess.extend([key] * value)
                
                for i in range(cypherLength):
                        keys = list(postitionDict[i].keys())
                        weights = list(postitionDict[i].values())
                        color = random.choices(keys, weights=weights, k=1)[0]
                        while color not in validColors:
                            color = random.choices(keys, weights=weights, k=1)[0]
                        guess.append(color)
                
                while contains_all_elements(guess, baseGuess) == False:
                    # print(cypher, baseGuess, guess)
                    guess = []
                    for i in range(cypherLength):
                        keys = list(postitionDict[i].keys())
                        weights = list(postitionDict[i].values())
                        color = random.choices(keys, weights=weights, k=1)[0]
                        while color not in validColors:
                            color = random.choices(keys, weights=weights, k=1)[0]
                        guess.append(color)
        # print(guess)
        guessHistory.append(guess)
        
        if cypher == guess:
            break
        turnCount += 1
        result = Turn(cypher, guess, colorDict)
        
        if result[0]+result[1] == 0:
            for i in range(len(guess)):
                if guess[i] in validColors:
                    validColors.remove(guess[i])
                    
        if result[0]+result[1] == cypherLength:
            validColors = []
            for i in range(len(guess)):
                validColors.append(guess[i])
                        
        for i in range(result[0]):
            for i in range(len(guess)):
                postitionDict[i][guess[i]] += .25
                
        # for i in range(result[1]):
        #     for i in range(len(guess)):
        #         for j in range(len(guess)):
        #             if guess[i] != guess[j]:
        #                 postitionDict[i][guess[j]] += .08
        
        for i in range(len(postitionDict)):
            valueTotal = 0
            for j in range(len(postitionDict[i])):
                valueTotal += postitionDict[i][colors[j]]
            if valueTotal != 0:
                for j in range(len(postitionDict[i])):
                    postitionDict[i][colors[j]] = postitionDict[i][colors[j]] / valueTotal
                    postitionDict[i][colors[j]] = round(postitionDict[i][colors[j]], 2)
                    
        if len(colors) != len(checkedColors):
            checkedColors.append(colors[len(checkedColors)])
            if result[0] > 0:
                validColorsAmounts[colors[len(checkedColors) - 1]] = result[0]
    # print("==============================")
    # print(cypher)
    # print("-----------------------------")
    # for i in range(len(postitionDict)):
    #     print(i, postitionDict[i])
    # print("-----------------------------")
    # print(turnCount)
    return turnCount

def Algo4(cypher,colorDict,colors,cypherLength):
    
    turnCount = 1
    guessHistory = []
    validColors = []
    postitionDict = {}
    
    for i in range(len(colors)):
        validColors.append(colors[i])
    
    
    for i in range(cypherLength):
        postitionDict[i] = {}
        for j in range(len(colors)):
            postitionDict[i][colors[j]] = 0.001


    while turnCount < 10000:
        guess = []
        
        if turnCount < len(validColors) - cypherLength - 1:
            for i in range(cypherLength):
                guess.append(validColors[i + (turnCount - 1)])
                
        else:
            while guess in guessHistory:
                guess = []
                
                # for i in range(cypherLength):
                #     guess.append(random.choice(colors))
                
                for i in range(cypherLength):
                    keys = list(postitionDict[i].keys())
                    weights = list(postitionDict[i].values())
                    color = random.choices(keys, weights=weights, k=1)[0]
                    while color not in validColors:
                        color = random.choices(keys, weights=weights, k=1)[0]
                    guess.append(color)
        
        guessHistory.append(guess)
        
        if cypher == guess:
            break
        turnCount += 1
        result = Turn(cypher, guess, colorDict)
        
        if result[0]+result[1] == 0:
            for i in range(len(guess)):
                if guess[i] in validColors:
                    validColors.remove(guess[i])
                    
        if result[0]+result[1] == cypherLength:
            validColors = []
            for i in range(len(guess)):
                validColors.append(guess[i])
                        
        for i in range(result[0]):
            for i in range(len(guess)):
                postitionDict[i][guess[i]] += .25
                
        # for i in range(result[1]):
        #     for i in range(len(guess)):
        #         for j in range(len(guess)):
        #             if guess[i] != guess[j]:
        #                 postitionDict[i][guess[j]] += .08
        
        for i in range(len(postitionDict)):
            valueTotal = 0
            for j in range(len(postitionDict[i])):
                valueTotal += postitionDict[i][colors[j]]
            if valueTotal != 0:
                for j in range(len(postitionDict[i])):
                    postitionDict[i][colors[j]] = postitionDict[i][colors[j]] / valueTotal
                    postitionDict[i][colors[j]] = round(postitionDict[i][colors[j]], 2)
    # print("==============================")
    # print(cypher)
    # print("-----------------------------")
    # for i in range(len(postitionDict)):
    #     print(i, postitionDict[i])
    # print("-----------------------------")
    # print(turnCount)
    return turnCount


Algo45(CreateCypher(testCypherLength,testColors),testColorDict,testColors,testCypherLength)