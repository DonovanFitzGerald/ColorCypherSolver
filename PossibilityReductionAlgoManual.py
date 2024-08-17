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
        guess.append(colors[i % (int(len(colors) / 2))])
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


def calculateCheckedColors(notCheckedColors, remainingPossibilities, colors, guess):
    for color in guess:
        if color in notCheckedColors:
            notCheckedColors.remove(color)
        possibleColors = []
        for possibility in remainingPossibilities:
            if color in possibility:
                possibleColors.append(possibility)
        allColors = [color for color in colors]
        for possibility in possibleColors:
            if possibility in allColors:
                possibleColors.remove(possibility)
        for possibility in possibleColors:
            if possibility in notCheckedColors:
                notCheckedColors.remove(possibility)
    return notCheckedColors


def createGuess(remainingPossibilities, notCheckedColors):
    options = []
    for possibility in remainingPossibilities:
        if set(notCheckedColors).issubset(set(possibility)):
            options.append(possibility)
    if len(options) == 0:
        for possibility in remainingPossibilities:
            for color in notCheckedColors:
                if color in possibility:
                    if possibility not in options:
                        options.append(possibility)
    if len(options) == 0:
        guess = random.choice(remainingPossibilities)
    else:
        guess = random.choice(options)
    return guess


def PossibilityReductionManual(colors, cypherLength):
    remainingPossibilities = getAllPossibilities(colors, cypherLength)
    guessHistory = []
    turnCount = 0
    notCheckedColors = [color for color in colors]

    while turnCount < 10:
        if turnCount == 0:
            guess = getInitalGuesses(colors, cypherLength)
        else:
            guess = createGuess(remainingPossibilities, notCheckedColors)

        print("Guess: ", guess)

        # checkSolved = input("Is it solved? (y/n): ")
        # if checkSolved == "yes" or checkSolved == "y":
        #     print("Solved!")
        #     break

        correctPositionCount = int(input("Enter correct position count: "))
        correctColorCount = int(input("Enter correct color count: "))

        turnCount += 1

        feedback = [correctPositionCount, correctColorCount]

        guessHistory.append([guess, feedback])

        remainingPossibilities = removeGuessPossibilities(
            remainingPossibilities,
            colors,
            guessHistory,
        )

        notCheckedColors = calculateCheckedColors(
            notCheckedColors, remainingPossibilities, colors, guess
        )

    return turnCount


colors = ["R", "G", "B", "Y", "P", "W"]
cypherLength = 4

PossibilityReductionManual(colors, cypherLength)
