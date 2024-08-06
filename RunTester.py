import random
import numpy
from CypherCreator import *
from Game import *
from Turn import *
from SolveAlgo import *
import time

runs = 100000
printEvery = 10000

cypherLength = 4
guesses = 1
colors = ["R", "G", "B", "Y", "P", "W"]

turnDict = {}

colorDict = {}
for i in range(len(colors)):
    colorDict[colors[i]] = 0

start_time = time.time()

totalTurns = 0
i = runs
printEveryCurrent = 0
while i > 0:
    i -= 1
    cypher = CreateCypher(cypherLength,colors)
    # print(cypher)
    turns = Algo45(cypher, colorDict, colors, cypherLength)
    
    if turns in turnDict:
        turnDict[turns] += 1
    else:
        turnDict[turns] = 1
    
    if  printEveryCurrent == 0:
        print("Game: ", runs - i, "   Turns = ", turns)
        printEveryCurrent = printEvery
    printEveryCurrent -= 1
        
    totalTurns += turns
    
# print("Total Turns = ", totalTurns)
# print("Total Runs = ", runs)
turnsAverage = totalTurns / runs
print("-------------------------------------")
print("Average: ", turnsAverage, "turns")
print("-------------------------------------")
runtime = time.time() - start_time
print("runtime: ", round(runtime, 3),"s")
print("per run: ", round((runtime / runs) * 1000, 3) ," ms")
print("-------------------------------------")


# turnDict = dict(sorted(turnDict.items()))
# for i in turnDict:
#     print(i)
# print("-------------------------------------")
# for i in turnDict:
#     print(turnDict[i])