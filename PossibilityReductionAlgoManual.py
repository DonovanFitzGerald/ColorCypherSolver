import random
from Turn import Turn
from collections import Counter
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
        guess.append(colors[i])
    return guess


def removeGuessPossibilities(
    remainingPossibilities,
    colors,
    guessHistory,
):
    guess = guessHistory[len(guessHistory) - 1][0]

    possibilities = [p for p in remainingPossibilities if p != guess]

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


def PossibilityReductionManual(colors, cypherLength):
    remainingPossibilities = getAllPossibilities(colors, cypherLength)
    guessHistory = []
    turnCount = 1

    while turnCount < 10:
        guess = []

        if turnCount == 1:
            guess = getInitalGuesses(colors, cypherLength)
        else:
            guess = []
            guess = random.choice(remainingPossibilities)

        print("Guess: ", guess)

        checkSolved = input("Is it solved? (y/n): ")
        if checkSolved == "yes" or checkSolved == "y":
            print("Solved!")
            break

        correctPositionCount = int(input("Enter correct position count: "))
        correctColorCount = int(input("Enter correct color count: "))

        feedback = [correctPositionCount, correctColorCount]

        guessHistory.append([guess, feedback])

        remainingPossibilities = removeGuessPossibilities(
            remainingPossibilities,
            cypherLength,
            colors,
            guessHistory,
        )

    return turnCount


colors = ["R", "G", "B", "Y", "P", "W"]
cypherLength = 4

PossibilityReductionManual(colors, cypherLength)
