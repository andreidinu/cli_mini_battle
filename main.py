import random
from choice import player

target = open('log.txt', 'a')


def round_four(round_number):
    if round_number % 4 == 0:
        player[0].special = True
        player[1].special = True
    else:
        player[0].special = False
        player[1].special = False

    if player[0].special is True:
        if 0.0 <= random.random() < 0.50:
            print('Player 1 got the bonus!')
            target.write('Player 1 got the bonus!\n')
            player[0].bonus()

        else:
            print('Player 2 got the bonus!')
            target.write('Player 2 got the bonus!\n')
            player[1].bonus()


def check_options(turn):
    if player[turn].stamina >= 8:
        print("1. Attack")
        print("2. Special Ability")
        print("3. Stand Still")
        return 1, 2, 3
    elif 3 <= player[turn].stamina < 8:
        print('1. Attack')
        print('3. Stand Still')
        return 1, 3
    else:
        print('3. Stand Still')
        return 3

def print_status():
    print('\nPlayer 1: \n' + 'HP:', player[0].hp, '\nStamina:', player[0].stamina)
    print('\nPlayer 2: \n' + 'HP:', player[1].hp, '\nStamina:', player[1].stamina)


def player_turn(turn):
    inp = int(input())
    try:
        while inp not in check_options(turn):
            print("Choose one of available options!")
            inp = int(input())
    except TypeError:
        while inp != check_options(turn):
            print("Choose one of tha available options!")
            inp = int(input())

    if inp == 1:
            target.write('Player ' + str((turn + 1)) + ' attacks Player ' + str(((turn + 1) % 2 + 1)) + ' for {} '.format(player[turn % 2].attack) + ' damage.\n')
            player[(turn + 1) % 2].hp -= player[turn % 2].attack
            player[turn % 2].cost_stamina()
            print_status()

    elif inp == 2:
            target.write('Player ' + str(turn + 1) + ' uses his special ability to attack Player 2 for {} '.format(3 * player[turn % 2].attack) + ' damage.\n')
            player[(turn + 1) % 2].hp -= player[turn % 2].get_special_attack()
            player[turn % 2].cost_stamina_special_attack()
            print_status()
    else:
            target.write('Player ' + str(turn + 1) + ' stands. His HP and Stamina will regenerate.\n')
            player[turn % 2].regen_health()
            player[turn % 2].regen_stamina()
            print_status()


def check_winner():
    print('------------------------------------------------')
    if player[0].hp <= 0:
        print('Player 2 wins!')
        target.write('Player 1 has no more life. Player 2 wins!')
    else:
        print('Player 1 wins!')
        target.write('Player 2 has no more life. Player 1 wins!')


def print_round(round_number):
    print('------------------------------------------------')
    print('Round number', round_number)
    print('------------------------------------------------')


def main():
    round_number = 1
    while player[0].hp > 0 and player[1].hp > 0:
        print_round(round_number)
        print_status()
        round_four(round_number)

        print('\nPlayer\'s 1 turn: ')
        turn = 0
        check_options(turn)
        player_turn(turn)

        if player[1].hp <= 0:
            check_winner()
            break

        print('\nPlayer\'s 2 turn: ')
        turn = 1
        check_options(turn)
        player_turn(turn)

        if player[0].hp <= 0:
            check_winner()
            break

        round_number += 1

if __name__ == "__main__":
    main()

target.close()
