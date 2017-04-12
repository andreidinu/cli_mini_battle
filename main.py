instructions = open('instructions.txt', 'r')
print(instructions.read())

import random
import fighters
from choice import player_1, player_2


target = open('log.txt', 'a')
round_number = 1

while player_1.hp > 0 and player_2.hp > 0:

    # Turns on the bonus every 4 rounds
    if round_number % 4 == 0:
        player_1.special = True
        player_2.special = True
    else:
        player_1.special = False
        player_2.special = False

    print('------------------------------------------------')
    print('Round number', round_number)
    print('------------------------------------------------')



    # Random offer the bonus to a player or another

    if player_1.special is True and player_2.special:
        if 0.0 <= random.random() < 0.5:
            print('Player 1 got the bonus!')
            target.write('Player 1 got the bonus!\n')
            if isinstance(player_1, fighters.Rogue):
                player_2.hp -= 1
                player_1.hp += 2
                player_1.stamina += 2
            elif isinstance(player_1, fighters.Shaman):
                player_1.hp += 3
                player_1.stamina += 3
            elif isinstance(player_1, fighters.Hunter):
                player_2.hp -= 4
            elif isinstance(player_1, fighters.Priest):
                player_1.hp += 3
                player_1.stamina += 3
            elif isinstance(player_1, fighters.Warrior):
                player_2.hp -= 4
        else:
            print('Player 2 got the bonus!')
            target.write('Player 2 got the bonus!\n')
            if isinstance(player_2, fighters.Rogue):
                player_1.hp -= 1
                player_2.hp += 2
                player_1.stamina += 2
            elif isinstance(player_2, fighters.Shaman):
                player_2.hp += 3
                player_2.stamina += 3
            elif isinstance(player_2, fighters.Hunter):
                player_1.hp -= 4
            elif isinstance(player_2, fighters.Priest):
                player_2.hp += 3
                player_2.stamina += 3
            elif isinstance(player_2, fighters.Warrior):
                player_1.hp -= 4

    print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
    print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

    # Checks available options for first player
    if player_1.stamina >= 8:
        print('\nPlayer\'s 1 turn: ')
        print('1. Attack')
        print('2. Special Ability')
        print('3. Stand Still')

        inp = int(input())
        if inp == 1:
            target.write('Player 1 attacks Player 2 for {} '.format(player_1.attack) + 'damage.\n')
            player_2.hp -= player_1.attack
            player_1.stamina -= 3

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        elif inp == 2:
            target.write('Player 1 uses his special ability to attack Player 2 for {} '.format(3 * player_1.attack) + 'damage.\n')
            player_2.hp -= 3 * player_1.attack
            player_1.stamina -= 8

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        else:
            target.write('Player 1 stands. His HP and Stamina will regenerate.\n')
            player_1.hp += 2
            player_1.stamina += 2

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        if player_2.hp <= 0:
            break

    elif 3 <= player_1.stamina < 8:
        print('\nPlayer\'s 1 turn: ')
        print('1. Attack')
        print('3. Stand Still')

        inp = int(input())
        if inp == 1:
            target.write('Player 1 attacks Player 2 for {} '.format(player_1.attack) + 'damage.\n')
            player_2.hp -= player_1.attack
            player_1.stamina -= 3

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        else:
            target.write('Player 1 stands. His HP and Stamina will regenerate.\n')
            player_1.hp += 2
            player_1.stamina += 2

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        if player_2.hp <= 0:
            break

    else:
        print('\nPlayer\'s 1 turn:')
        print('3. Stand still')

        inp = int(input())
        if inp == 3:
            target.write('Player 1 stands. His HP and Stamina will regenerate.\n')
            player_1.hp += 2
            player_1.stamina += 2

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        if player_2.hp <= 0:
            break

    # Checks available options for player 2
    if player_2.stamina >= 8:
        print('\nPlayer\'s 2 turn: ')
        print('1. Attack')
        print('2. Special Ability')
        print('3. Stand Still')

        inp = int(input())
        if inp == 1:
            target.write('Player 2 attacks Player 1 for {} '.format(player_2.attack) + 'damage.\n')
            player_1.hp -= player_2.attack
            player_2.stamina -= 3

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        elif inp == 2:
            target.write('Player 2 uses his special ability to attack Player 1 for {} '.format(3 * player_1.attack) + 'damage.\n')
            player_1.hp -= 3 * player_1.attack
            player_2.stamina -= 8

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        else:
            target.write('Player 2 stands. His HP and Stamina will regenerate.\n')
            player_2.hp += 2
            player_2.stamina += 2

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        if player_1.hp <= 0:
            break

    elif 3 <= player_2.stamina < 8:
        print('\nPlayer\'s 2 turn: ')
        print('1. Attack')
        print('3. Stand Still')

        inp = int(input())
        if inp == 1:
            target.write('Player 2 attacks Player 1 for {} '.format(player_2.attack) + 'damage.\n')
            player_1.hp -= player_2.attack
            player_2.stamina -= 3

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        else:
            target.write('Player 2 stands. His HP and Stamina will regenerate.\n')
            player_2.hp += 2
            player_2.stamina += 2

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)
    else:
        print('\nPlayer\'s 2 turn: ')
        print('3. Stand Still')

        inp = int(input())
        if inp == 3:
            target.write('Player 2 stands. His HP and Stamina will regenerate.\n')
            player_2.hp += 2
            player_2.stamina += 2

            print('\nPlayer 1: \n' + 'HP:', player_1.hp, '\nStamina:', player_1.stamina)
            print('\nPlayer 2: \n' + 'HP:', player_2.hp, '\nStamina:', player_2.stamina)

        if player_1.hp <= 0:
            break
    round_number += 1

print('------------------------------------------------')
if player_1.hp <= 0:
    print('Player 2 wins!')
    target.write('Player 1 has no more life. Player 2 wins!')
else:
    print('Player 1 wins!')
    target.write('Player 2 has no more life. Player 1 wins!')

target.close()

