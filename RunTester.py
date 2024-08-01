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
i = runs
while i > 0:
    i -= 1
    cypher = CreateCypher(cypherLength,colors)
    print(cypher)
    turns += Game(cypher, colorDict, colors, cypherLength)
    
print("Total Turns = ", turns)
print("Total Runs = ", runs)
turnsAverage = turns / runs
print("Average = ", turnsAverage)