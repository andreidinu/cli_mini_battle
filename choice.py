import fighters

print("Select the 2 characters types out of this: \n")
print("1. Rogue")
print("2. Shaman")
print("3. Hunter")
print("4. Priest")
print("5. Warrior")

player_1 = int(input('Choose the first character: '))

target = open('log.txt', 'w')

if player_1 == 1:
    print('Player 1 has chosen Rogue.')
    target.write('Player 1 has chosen Rogue.\n')
    rogue_1 = fighters.Rogue(10, 9, 3, False)
    player_1 = rogue_1

elif player_1 == 2:
    print('Player 1 has chosen Shaman.')
    target.write('Player 1 has chosen Shaman.\n')
    shaman_1 = fighters.Shaman(30, 15, 3, False)
    player_1 = shaman_1

elif player_1 == 3:
    print('Player 1 has chosen Hunter.')
    target.write('Player 1 has chosen Hunter.\n')
    hunter_1 = fighters.Hunter(30, 15, 4, False)
    player_1 = hunter_1

elif player_1 == 4:
    print('Player 1 has chosen Priest.')
    target.write('Player 1 has chosen Priest.\n')
    priest_1 = fighters.Priest(30, 20, 2, False)
    player_1 = priest_1

elif player_1 == 5:
    print('Player 1 has chosen Warrior.')
    target.write('Player 1 has chosen Warrior.\n')
    warrior_1 = fighters.Warrior(30, 15, 4, False)
    player_1 = warrior_1


player_2 = int(input('Choose the second character: '))

if player_2 == 1:
    print('Player 2 has chosen Rogue.')
    target.write('Player 2 has chosen Rogue.\n')
    rogue_2 = fighters.Rogue(30, 15, 3, False)
    player_2 = rogue_2

elif player_2 == 2:
    print('Player 2 has chosen Shaman.')
    target.write('Player 2 has chosen Shaman.\n')
    shaman_2 = fighters.Shaman(30, 15, 3, False)
    player_2 = shaman_2

elif player_2 == 3:
    print('Player 2 has chosen Hunter.')
    target.write('Player 2 has chosen Hunter.\n')
    hunter_2 = fighters.Hunter(3, 15, 4, False)
    player_2 = hunter_2

elif player_2 == 4:
    print('Player 2 has chosen Priest.')
    target.write('Player 2 has chosen Priest.\n')
    priest_2 = fighters.Priest(30, 20, 2, False)
    player_2 = priest_2

elif player_2 == 5:
    print('Player 2 has chosen Warrior.')
    target.write('Player 2 has chosen Warrior.\n')
    warrior_2 = fighters.Warrior(30, 15, 4, False)
    player_2 = warrior_2

target.close()
