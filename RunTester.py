from CypherCreator import CreateCypher
# from Game import Game

# from SolveAlgo import *
import time
from PossibilityReductionAlgo import PossibilityReductionAlgo

runs = 100000
printEvery = 1000

cypherLength = 2
colors = ["R", "G", "B", "Y", "P", "W"]

turnDict = {}

start_time = time.time()

totalTurns = 0
i = runs
printEveryCurrent = 0
while i > 0:
    i -= 1
    cypher = CreateCypher(cypherLength, colors)
    # print(cypher)
    turns = PossibilityReductionAlgo(cypher, colors, cypherLength)

    if turns in turnDict:
        turnDict[turns] += 1
    else:
        turnDict[turns] = 1

    if printEveryCurrent == 0:
        print("Game: ", runs - i, "   Turns = ", turns)
        printEveryCurrent = printEvery
    printEveryCurrent -= 1

    totalTurns += turns

turnsAverage = totalTurns / runs
print("-------------------------------------")
print("Average: ", turnsAverage, "turns")
print("-------------------------------------")
runtime = time.time() - start_time
print("runtime: ", round(runtime, 3), "s")
print("per run: ", round((runtime / runs) * 1000, 3), " ms")
print("-------------------------------------")


turnDict = dict(sorted(turnDict.items()))
for i in turnDict:
    print(i)
print("-------------------------------------")
for i in turnDict:
    print(turnDict[i])
