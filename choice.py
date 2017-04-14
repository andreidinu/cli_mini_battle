import fighters

player = [0, 0]

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
    if player[i] == 1:
        print('Player', (i + 1), 'has chosen Rogue.')
        target.write('Player ' + str(i + 1) + ' has chosen Rogue.\n')
        player[i] = fighters.Rogue(30, 15, 3, False)

    elif player[i] == 2:
        print('Player', (i + 1), 'has chosen Shaman.')
        target.write('Player ' + str(i + 1) + ' has chosen Shaman.\n')
        player[i] = fighters.Shaman(30, 15, 3, False)

    elif player[i] == 3:
        print('Player', (i + 1), 'has chosen Hunter.')
        target.write('Player ' + str(i + 1) + ' has chosen Hunter.\n')
        player[i] = fighters.Hunter(30, 15, 4, False)

    elif player[i] == 4:
        print('Player', (i + 1), 'has chosen Priest.')
        target.write('Player ' + str(i + 1) + ' has chosen Priest.\n')
        player[i] = fighters.Priest(30, 20, 2, False)

    elif player[i] == 5:
        print('Player', (i + 1), 'has chosen Warrior.')
        target.write('Player ' + str(i + 1) + ' has chosen Warrior.\n')
        player[i] = fighters.Warrior(30, 15, 4, False)


target.close()
