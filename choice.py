from fighters import *

player = [0, 0]
hero_dict = {2: Shaman(30, 15, 3, False), 1: Rogue(30, 15, 3, False), 3: Hunter(30, 15, 4, False),
        4: Priest(30, 20, 2, False), 5: Warrior(30, 15, 4, False)}

print("Select the 2 characters types out of this: \n")
print("1. Rogue")
print("2. Shaman")
print("3. Hunter")
print("4. Priest")
print("5. Warrior")

player[0] = int(input('Choose the first character: '))
player[1] = int(input('Choose the second character: '))

target = open('log.txt', 'w')

for i in range(len(player)):
    player[i] = hero_dict[player[i]]

target.close()
