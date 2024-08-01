import Turn

def CheckValid(guess,colors,cypherLength):
    if len(guess) != cypherLength:
        return False
    for i in range(len(guess)):
        if guess[i] not in colors:
            return False
    return True


def Game(cypherLength,guesses,colors,cypher):
    currentGuess = 0

    cypherDict = colorDict.copy()
    for i in range(len(cypher)):
        cypherDict[cypher[i]] += 1
    
    while currentGuess < guesses:
            print("Guess", currentGuess + 1, "of", guesses)
            currentGuess += 1
            print("Enter your guess: ")
            guess = list(input().upper())
            valid = True
            
            if len(guess) != cypherLength:
                valid = False
                break
            else:
                for i in range(len(guess)):
                    if guess[i] not in colors:
                        valid = False
                        break

            if valid == False:
                print("! INVALID GUESS ! TRY AGAIN !")
                continue
            
            guessTotals = colorDict.copy()
            for i in range(len(guess)):
                guessTotals[guess[i]] += 1 

            correctSpots = colorDict.copy()
            somewhereSpots = colorDict.copy()
            for i in range(len(guess)):
                if guess[i] == cypher[i]:
                    correctSpots[guess[i]] += 1
                elif guess[i] in cypher:
                    somewhereSpots[guess[i]] += 1

            correctSpotsTotal = 0
            somewhereSpotsTotal = 0
            for i in somewhereSpots:
                if cypherDict[i] == 0:
                    continue
                elif cypherDict[i] == correctSpots[i]:
                    correctSpotsTotal += correctSpots[i]
                    continue
                elif cypherDict[i] >= correctSpots[i]:
                    correctSpotsTotal += correctSpots[i]
                    if cypherDict[i] <= somewhereSpots[i]:
                        somewhereSpotsTotal += cypherDict[i] - correctSpots[i]
                    else:
                        somewhereSpotsTotal += somewhereSpots[i]
                    continue

            print("===========================================================")
            print("Your Guess: ", guess)
            print("Correct: ", correctSpotsTotal, "  In Cypher: ", somewhereSpotsTotal)
            if cypher == guess:
                print("YOU WIN!")
                print ("Total tries:", currentGuess + 1, "guesses")
                print("===========================================================")
                break
            print("===========================================================")
        print("GAME OVER")
        return currentGuess