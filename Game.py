from Turn import *
from SolveAlgo import *

def CheckValid(guess,colors,cypherLength):
    if len(guess) != cypherLength:
        return False
    for i in range(len(guess)):
        if guess[i] not in colors:
            return False
    return True


def Game(cypher,colorDict,colors, cypherLength):
    turnCount = 1
    while True:
        # print("turn: ",turnCount)
        # print("Enter guess: ")
        # guess = list(input().upper())
        guess = AlgoOne(colors, cypherLength)

        Turn(cypher, guess, colorDict) 
        
        if cypher == guess:
            break
        turnCount += 1
        
    # print("===========================================================")
    # print("YOU WIN!")
    # print ("Total tries:", turnCount, "guesses")
    # print("===========================================================")
    return turnCount