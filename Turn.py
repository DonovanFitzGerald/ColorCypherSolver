import time

testColorsDict = {"R": 0, "G": 0, "B": 0, "Y": 0, "P": 0, "W": 0}
testCypher = ["R", "G", "Y", "W"]
testGuess = ["R", "R", "W", "R"]


def Turn(cypher, guess, colors):
    if len(guess) != len(cypher):
        print("Invalid guess")
        return

    colorDict = {color: 0 for color in colors}

    guessTotals = colorDict.copy()
    cypherDict = colorDict.copy()
    correctSpotsTotal, somewhereSpotsTotal = 0, 0

    for i in range(len(guess)):
        guessTotals[guess[i]] += 1
        cypherDict[cypher[i]] += 1
        if guess[i] == cypher[i]:
            correctSpotsTotal += 1

    for color in colors:
        if cypherDict[color] > 0:
            somewhereSpotsTotal += min(guessTotals[color], cypherDict[color])
    somewhereSpotsTotal -= correctSpotsTotal

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
