import time

testColorsDict = {"R": 0, "G": 0, "B": 0, "Y": 0, "P": 0, "W": 0}
testCypher = ["R", "G", "Y", "W"]
testGuess = ["R", "R", "W", "R"]


def Turn(cypher, guess, colorDict):
    if len(guess) != len(cypher):
        print("Invalid guess")
        return
    guessTotals = colorDict.copy()
    for i in range(len(guess)):
        guessTotals[guess[i]] += 1

    cypherDict = colorDict.copy()
    for i in range(len(cypher)):
        cypherDict[cypher[i]] += 1

    correctSpots = colorDict.copy()
    somewhereSpots = colorDict.copy()
    for i in range(len(guess)):
        if guess[i] == cypher[i]:
            correctSpots[guess[i]] += 1
        elif guess[i] in cypher:
            somewhereSpots[guess[i]] += 1

    correctSpotsTotal = 0
    somewhereSpotsTotal = 0
    for i in somewhereSpots:
        if cypherDict[i] == 0:
            continue
        elif cypherDict[i] == correctSpots[i]:
            correctSpotsTotal += correctSpots[i]
            continue
        elif cypherDict[i] >= correctSpots[i]:
            correctSpotsTotal += correctSpots[i]
            if cypherDict[i] <= somewhereSpots[i]:
                somewhereSpotsTotal += cypherDict[i] - correctSpots[i]
            else:
                somewhereSpotsTotal += somewhereSpots[i]
            continue

    guessString = ""
    for i in range(len(guess)):
        guessString += guess[i]
        guessString += " "

    # print("--------------------------------------------------------------------------")
    # print("Your Guess: ", guessString)
    # print("Correct: ", correctSpotsTotal)
    # print("In Cypher: ", somewhereSpotsTotal)
    # print("--------------------------------------------------------------------------")

    return [correctSpotsTotal, somewhereSpotsTotal]


# def Test():
#     totalRuns = 100000
#     runs = totalRuns
#     start_time = time.time()
#     while runs > 0:
#         runs -= 1
#         result = Turn(testCypher, testGuess, testColorsDict)
#         print(result)
#         runtime = time.time() - start_time
#     print("runtime: ", runtime / totalRuns,"s")

# Test()
