from Turn import *

def CheckValid(guess,colors,cypherLength):
    if len(guess) != cypherLength:
        return False
    for i in range(len(guess)):
        if guess[i] not in colors:
            return False
    return True


def Game(guesses,cypher,colorDict):
    currentGuess = 0
    while currentGuess < guesses:
        print("Guess", currentGuess + 1, "of", guesses)
        print("Enter your guess: ")
        guess = list(input().upper())
        currentGuess += 1
        
        Turn(cypher, guess, colorDict)
        
        if cypher == guess:
            print("YOU WIN!")
            print ("Total tries:", currentGuess, "guesses")
            print("===========================================================")
            break
        print("===========================================================")
        print("GAME OVER")
        break
    return currentGuess