import random

def AlgoOne(colors, cypherLength):
    guess = []
    for i in range(cypherLength):
        guess.append(random.choice(colors))
    return guess