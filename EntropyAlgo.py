import random
from Turn import Turn
from collections import Counter, defaultdict
from itertools import product
import numpy

testColors = ["R", "G", "B", "Y", "P", "W"]
testColorDict = {"R": 0, "G": 0, "B": 0, "Y": 0, "P": 0, "W": 0}
testCypher = ["R", "G", "Y", "W"]
testCypherLength = 4


def CreateCypher(cypherLength, colors):
    cypher = []
    while len(cypher) < cypherLength:
        i = random.randint(0, 5)
        cypher.append(colors[i])
    return cypher


def getPositionProbabiltyDict(allPossibilities, cypherLength, colors):
    positionPossibilitiesDict = {}
    for i in range(cypherLength):
        positionPossibilitiesDict[i] = {}
        for j in range(len(colors)):
            positionPossibilitiesDict[i][colors[j]] = 0
    for i in range(len(allPossibilities)):
        for j in range(len(allPossibilities[i])):
            positionPossibilitiesDict[j][allPossibilities[i][j]] += 1
    # for i in range(len(positionPossibilitiesDict)):
    #     print(i, positionPossibilitiesDict[i])
    return positionPossibilitiesDict


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
        guess.append(colors[i])
    return guess


def removeGuessPossibilities(
    remainingPossibilities,
    guess,
    feedback,
    cypherLength,
    colors,
    guessHistory,
    correctColorPositionsArray,
    wrongColorPositionsArray,
):
    possibilities = [p for p in remainingPossibilities if p != guess]

    guessSet = set(guess)

    if feedback[0] + feedback[1] == 0:
        possibilities = [p for p in possibilities if not guessSet.intersection(p)]

    elif feedback[0] + feedback[1] == cypherLength:
        guessDict = dict(sorted(Counter(guess).items()))
        possibilities = [
            p for p in possibilities if dict(sorted(Counter(p).items())) == guessDict
        ]

    # Remove possibilities based on historical feedback
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


def EntropyAlgo(cypher, colors, cypherLength):
    allPossibilities = getAllPossibilities(colors, cypherLength)
    remainingPossibilities = allPossibilities.copy()
    # positionPossibilitiesDict = getPositionProbabiltyDict(
    #     allPossibilities, cypherLength, colors
    # )
    guessHistory = []

    correctColorPositionsArray = []
    wrongColorPositionsArray = []
    for i in range(cypherLength):
        correctColorPositionsArray.append([])
    for i in range(cypherLength):
        wrongColorPositionsArray.append([])

    turnCount = 0
    while turnCount < 10000:
        guess = []

        if turnCount == 1:
            guess = getInitalGuesses(colors, cypherLength)
        else:
            if len(remainingPossibilities) == 1:
                guess = remainingPossibilities[0]
            else:
                guess = []
                guess = random.choice(remainingPossibilities)

        if guess not in remainingPossibilities:
            guess = []
            guess = random.choice(remainingPossibilities)

        # print(cypher, guess)

        feedback = Turn(cypher, guess, colors)
        turnCount += 1
        if cypher == guess:
            break

        guessHistory.append([guess, feedback])

        remainingPossibilities = removeGuessPossibilities(
            remainingPossibilities,
            guess,
            feedback,
            cypherLength,
            colors,
            guessHistory,
            correctColorPositionsArray,
            wrongColorPositionsArray,
        )

    return turnCount


EntropyAlgo(
    CreateCypher(testCypherLength, testColors),
    testColors,
    testCypherLength,
)
