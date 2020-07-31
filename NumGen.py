import random

#Picks a random characteristic and an animal
with open("chara.txt", "r", encoding="utf8") as f:
    character = random.choice(f.readlines()).rstrip()

with open("animals.txt", "r", encoding="utf8") as f:
    animal = random.choice(f.readlines()).rstrip()

with open("symbols.txt", "r", encoding="utf8") as f:
    symbols = random.choice(f.readlines()).rstrip()

#Picks a random number
Num = random.randrange(1, 101)

Pass = (character + animal + symbols)
print("Here is your password:")
print(Pass + str(Num))
#print("Copy the password and print it without the space.")