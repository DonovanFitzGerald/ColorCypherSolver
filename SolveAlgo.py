import random
from Turn import *

testColors = ["R", "G", "B", "Y", "P", "W"]
testColorDict = {"R": 0, "G": 0, "B": 0, "Y": 0, "P": 0, "W": 0}
testCypher = ["R", "G", "Y", "W"]
testCypherLength = 4

def AlgoOne(cypher,colorDict,colors, cypherLength):
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





def AlgoTwo(cypher,colorDict,colors,cypherLength):
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

def AlgoThree(cypher,colorDict,colors,cypherLength):
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



AlgoThree(testCypher,testColorDict,testColors,testCypherLength)