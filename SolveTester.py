import random
import numpy
from CypherCreator import *
from Game import *
from Turn import *

runs = 2

cypherLength = 4
guesses = 10
colors = ["R", "G", "B", "Y", "P", "W"]

colorDict = {}
for i in range(len(colors)):
    colorDict[colors[i]] = 0

turns = 0
totalRuns = runs
while runs > 0:
    runs -= 1
    cypher = CreateCypher(cypherLength,colors)
    print(cypher)
    turns += Game(guesses, cypher, colorDict)
    
print("Total Turns = ", turns)
print("Total Runs = ", totalRuns)
turnsAverage = turns / totalRuns
print("Average = ", turnsAverage)