import numpy
from collections import Counter

guess = ["R", "R", "W", "R"]
print(Counter(guess))


def getInitalGuesses(colors, cypherLength, turnCount):
    guess = []
    for i in range(cypherLength):
        guess.append(
            colors[(i + (turnCount * (len(colors) - cypherLength))) % len(colors)]
        )
    return guess

        if turnCount <= len(colors) - cypherLength - 1:
            guess = getInitalGuesses(colors, cypherLength, turnCount)
            
            
            
            
            
def generateGuess(possibilities, colors, guessHistory):
    possibilitiesStartLength = len(possibilities)
    possibilityReductionDict = {}
    for i in range(possibilitiesStartLength):
        possibility = possibilities[i]
        currentPossibilityRemaining = [p for p in possibilities]
        runningRemaining = 0
        for guessPossibility in possibilities:
            possibilityguessHistory = [g for g in guessHistory]
            feedback = Turn(possibility, guessPossibility, colors)
            possibilityguessHistory.append([guessPossibility, feedback])
            currentPossibilityRemaining = removeGuessPossibilities(
                currentPossibilityRemaining, colors, possibilityguessHistory
            )
            if len(currentPossibilityRemaining) <= 1:
                continue
            runningRemaining += len(currentPossibilityRemaining)
        possibilityReductionDict[i] = runningRemaining
        bestGuessIndex = min(possibilityReductionDict, key=possibilityReductionDict.get)
        bestGuess = possibilities[bestGuessIndex]
    return bestGuess