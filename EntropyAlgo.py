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
        guess.append(colors[0])
    return guess


def precomputeFeedbackTable(allPosibilities, colors):
    feedbackTable = {}
    for i in range(len(allPosibilities)):
        for j in range(i + 1, len(allPosibilities)):
            print(allPosibilities[i], allPosibilities[j])
            feedback = Turn(allPosibilities[j], allPosibilities[i], colors)
            feedback = (feedback[0], feedback[1])
            feedbackTable[allPosibilities[i]] = [allPosibilities[j]]
            feedbackTable[allPosibilities[j]][allPosibilities[i]] = feedback
    return feedbackTable


def removeGuessPossibilities(
    remainingPossibilities, guess, feedback, cypherLength, colors
):
    if guess in remainingPossibilities:
        remainingPossibilities.remove(guess)

    if feedback[0] + feedback[1] == 0:
        remainingPossibilities = [
            possibility
            for possibility in remainingPossibilities
            if not any(color in guess for color in possibility)
        ]

    if feedback[0] + feedback[1] == cypherLength:
        for i in range(len(guess)):
            guessDict = Counter(guess)
            guessDict = dict(sorted(guessDict.items()))
            for possibility in remainingPossibilities:
                possibilityDict = Counter(possibility)
                possibilityDict = dict(sorted(possibilityDict.items()))
                if possibilityDict != guessDict:
                    remainingPossibilities.remove(possibility)

    for possibility in remainingPossibilities:
        posibilityFeedback = Turn(guess, possibility, colors)
        if posibilityFeedback != feedback:
            remainingPossibilities.remove(possibility)

    return remainingPossibilities


def generateGuess(allPossibilities, remainingPossibilities, cypherLength, colors):
    turnGuessInformationDict = {}
    for i in range(len(allPossibilities)):
        testPossibilities = remainingPossibilities.copy()
        averagePossibilities = 0

        for j in range(len(remainingPossibilities)):
            feedback = Turn(allPossibilities[i], remainingPossibilities[j], colors)
            newPossibilities = removeGuessPossibilities(
                testPossibilities, allPossibilities[i], feedback, cypherLength, colors
            )
            averagePossibilities += len(newPossibilities)

        turnGuessInformationDict[i] = averagePossibilities
    mostInformationIndex = min(
        turnGuessInformationDict, key=turnGuessInformationDict.get
    )
    guess = allPossibilities[mostInformationIndex]
    return guess


def EntropyAlgo(cypher, colors, cypherLength):
    allPossibilities = getAllPossibilities(colors, cypherLength)
    remainingPossibilities = getAllPossibilities(colors, cypherLength)
    # positionPossibilitiesDict = getPositionProbabiltyDict(
    #     allPossibilities, cypherLength, colors
    # )
    turnCount = 0
    while turnCount < 10000:
        guess = []

        if turnCount <= 1:
            guess = getInitalGuesses(colors, cypherLength)

        elif len(remainingPossibilities) == 1:
            guess = remainingPossibilities[0]

        else:
            guess = generateGuess(
                allPossibilities, remainingPossibilities, cypherLength, colors
            )

        # print(cypher, guess)

        feedback = Turn(cypher, guess, colors)
        turnCount += 1
        if cypher == guess:
            break

        remainingPossibilities = removeGuessPossibilities(
            remainingPossibilities, guess, feedback, cypherLength, colors
        )

    return turnCount


# EntropyAlgo(
#     CreateCypher(testCypherLength, testColors),
#     testColors,
#     testCypherLength,
# )
