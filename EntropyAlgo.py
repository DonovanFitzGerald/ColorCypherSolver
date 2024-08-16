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


def getAllPossibilities(cypher, colorDict, colors, cypherLength):
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
        guess.append(colors[0])
    return guess


def precomputeFeedbackTable(allPosibilities, colorDict):
    feedbackTable = {}
    for i in range(len(allPosibilities)):
        for j in range(i + 1, len(allPosibilities)):
            print(allPosibilities[i], allPosibilities[j])
            feedback = Turn(allPosibilities[j], allPosibilities[i], colorDict)
            feedback = (feedback[0], feedback[1])
            feedbackTable[allPosibilities[i]] = [allPosibilities[j]]
            feedbackTable[allPosibilities[j]][allPosibilities[i]] = feedback
    return feedbackTable


def removeGuessPossibilities(
    allPossibilities, guess, feedback, cypherLength, colorDict
):
    if guess in allPossibilities:
        allPossibilities.remove(guess)

    if feedback[0] + feedback[1] == 0:
        allPossibilities = [
            possibility
            for possibility in allPossibilities
            if not any(color in guess for color in possibility)
        ]

    if feedback[0] + feedback[1] == cypherLength:
        for i in range(len(guess)):
            guessDict = Counter(guess)
            guessDict = dict(sorted(guessDict.items()))
            for possibility in allPossibilities:
                possibilityDict = Counter(possibility)
                possibilityDict = dict(sorted(possibilityDict.items()))
                if possibilityDict != guessDict:
                    allPossibilities.remove(possibility)

    for possibility in allPossibilities:
        posibilityFeedback = Turn(guess, possibility, colorDict)
        if posibilityFeedback != feedback:
            allPossibilities.remove(possibility)


def EntropyAlgo(cypher, colorDict, colors, cypherLength):
    allPossibilities = getAllPossibilities(cypher, colorDict, colors, cypherLength)
    positionPossibilitiesDict = getPositionProbabiltyDict(
        allPossibilities, cypherLength, colors
    )
    turnCount = 0
    while turnCount < 10000:
        guess = []

        if turnCount <= 1:
            guess = getInitalGuesses(colors, cypherLength)

        else:
            guess = random.choice(allPossibilities)

        if guess not in allPossibilities:
            guess = []
            guess = random.choice(allPossibilities)

        # print(cypher, guess)

        feedback = Turn(cypher, guess, colorDict)
        turnCount += 1
        if cypher == guess:
            break

        removeGuessPossibilities(
            allPossibilities, guess, feedback, cypherLength, colorDict
        )

        print(precomputeFeedbackTable(allPossibilities, colorDict))

    return turnCount


EntropyAlgo(
    CreateCypher(testCypherLength, testColors),
    testColorDict,
    testColors,
    testCypherLength,
)
