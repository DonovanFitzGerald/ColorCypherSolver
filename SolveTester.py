import random
import numpy
from CypherCreator import *
from Game import *
from Turn import *

totalRuns = 1

cypherLength = 4
guesses = 10
colors = ["R", "G", "B", "Y", "P", "W"]

colorDict = {}
for i in range(len(colors)):
    colorDict[colors[i]] = 0

turns = 0
while totalRuns > 0:
    totalRuns -= 1
    cypher = CreateCypher(cypherLength,colors)
    print(cypher)
    Game(cypher, colors, colorDict)
    
turnsAverage = turns / totalRuns
print("test = ", turnsAverage)