import random
from Turn import Turn
from itertools import product


def getAllPossibilities(colors, cypherLength):
    allPossibilitiesTuples = list(product(colors, repeat=cypherLength))
    allPossibilities = []
    for posibility in allPossibilitiesTuples:
        possibilityArray = []
        for i in range(len(posibility)):
            possibilityArray.append(posibility[i])
        allPossibilities.append(possibilityArray)
    return allPossibilities


def getInitalGuesses(colors, cypherLength):
    guess = []
    for i in range(cypherLength):
        guess.append(colors[i % len(colors)])
    return guess


def removeGuessPossibilities(
    remainingPossibilities,
    colors,
    guessHistory,
):
    guess = guessHistory[len(guessHistory) - 1][0]

    possibilities = [
        possibility for possibility in remainingPossibilities if possibility != guess
    ]

    validPossibilities = []
    for possibility in possibilities:
        valid = True
        for pastGuess, pastFeedback in guessHistory:
            if Turn(pastGuess, possibility, colors) != pastFeedback:
                valid = False
                break
        if valid:
            validPossibilities.append(possibility)

    possibilities = validPossibilities

    return possibilities


def PossibilityReductionAlgo(cypher, colors, cypherLength):
    remainingPossibilities = getAllPossibilities(colors, cypherLength)
    guessHistory = []
    turnCount = 0

    while turnCount < 10000:
        if turnCount == 1:
            guess = getInitalGuesses(colors, cypherLength)
        else:
            guess = random.choice(remainingPossibilities)

        feedback = Turn(cypher, guess, colors)
        turnCount += 1
        if cypher == guess:
            break

        guessHistory.append([guess, feedback])

        remainingPossibilities = removeGuessPossibilities(
            remainingPossibilities,
            colors,
            guessHistory,
        )

    return turnCount


def createTest():
    testColors = ["R", "G", "B", "Y", "P", "W"]
    testCypherLength = 4
    testCypher = []
    while len(testCypher) < testCypherLength:
        i = random.randint(0, 5)
        testCypher.append(testColors[i])
    return [testCypher, testColors, testCypherLength]


testparams = createTest()
PossibilityReductionAlgo(testparams[0], testparams[1], testparams[2])
