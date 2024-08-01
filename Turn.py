def Turn(cypher, guess, colorDict):
    guessTotals = colorDict.copy()
    for i in range(len(guess)):
        guessTotals[guess[i]] += 1 
        
    cypherDict = colorDict.copy()
    for i in range(len(cypher)):
        cypherDict[cypher[i]] += 1

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

    guessString = ""
    for i in range(len(guess)):
        guessString += guess[i]
        guessString += " "

    # print("--------------------------------------------------------------------------")
    # print("Your Guess: ", guessString)
    # print("Correct: ", correctSpotsTotal)
    # print("In Cypher: ", somewhereSpotsTotal)
    # print("--------------------------------------------------------------------------")
    
    result = [correctSpotsTotal, somewhereSpotsTotal]
    return result