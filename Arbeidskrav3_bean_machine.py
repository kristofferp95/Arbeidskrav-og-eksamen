import random

numberOfSlots = int(input(f'Enter number of slots: '))
numberOfBalls = int(input(f'Enter number of balls to drop: '))

slots = []
for i in range(0, numberOfSlots): 
    slots.append([])

for balls in range(0, numberOfBalls):
    points = 0 
    for k in range(0, numberOfSlots - 1): 
        direction = random.randint(0, 1)
        if direction == 0: 
            print(f'L', end= '')
        else: 
            print(f'R', end = '')
        points += direction
    slots[points].append(1)
    print()

biggest = 0
for c in range(0, len(slots)):
    maxNumber = sum(slots[c])
    if maxNumber > biggest: 
        biggest = maxNumber

for a in range(biggest, 0, -1):
    for z in range(0, numberOfSlots):
        if len(slots[z]) >= a: 
            print("o", end= '')
        else:
            print(' ', end= '')
    print()

    









