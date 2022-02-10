pets = ['dog','rabbit','goldfish','others','cat']


for pet in pets:
    print(pet)

for pet in pets:
    pets.remove(pet)

print(pets)

pets = ['dog','cat']

while pets:
    pets.pop()

print(f"The length of the pets list is now {len(pets)}.\n")