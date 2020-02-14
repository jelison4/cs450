import random
abilityScores=[]

def scoreRoll():
    rolls=[random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    rolls.remove(min(rolls))
    return sum(rolls)

good=False
while good!=True:
    abilityScores=[]
    count=0
    while count<6:
        abilityScore=scoreRoll()
        if abilityScore==18:
            good=True
        if len(abilityScores)==0:
            abilityScores=[abilityScore]
        else:
            abilityScores.append(abilityScore)
        count+=1

print(abilityScores)