import random
def CreateCypher(cypherLength,colors):    
    cypher = []
    while len(cypher) < cypherLength:
        i = random.randint(0, 5)
        cypher.append(colors[i])
    return cypher