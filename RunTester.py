import random
import numpy
from CypherCreator import *
from Game import *
from Turn import *
from SolveAlgo import *
import time

runs = 1000

cypherLength = 4
guesses = 10
colors = ["R", "G", "B", "Y", "P", "W"]

colorDict = {}
for i in range(len(colors)):
    colorDict[colors[i]] = 0

start_time = time.time()

totalTurns = 0
i = runs
while i > 0:
    i -= 1
    cypher = CreateCypher(cypherLength,colors)
    # print(cypher)
    turns = AlgoTwo(cypher, colorDict, colors, cypherLength)
    totalTurns += turns
    print("Game: ", runs - i, "   Turns = ", turns)
    
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