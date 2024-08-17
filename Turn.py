def Turn(cypher, guess, colors):
    if len(guess) != len(cypher):
        print("Invalid guess")
        return

    colorDict = {color: 0 for color in colors}

    guessTotals = colorDict.copy()
    cypherDict = colorDict.copy()
    correctSpotsTotal, somewhereSpotsTotal = 0, 0

    for i in range(len(guess)):
        guessTotals[guess[i]] += 1
        cypherDict[cypher[i]] += 1
        if guess[i] == cypher[i]:
            correctSpotsTotal += 1

    for color in colors:
        if cypherDict[color] > 0:
            somewhereSpotsTotal += min(guessTotals[color], cypherDict[color])
    somewhereSpotsTotal -= correctSpotsTotal

    guessString = ""
    for i in range(len(guess)):
        guessString += guess[i]
        guessString += " "

    return [correctSpotsTotal, somewhereSpotsTotal]
