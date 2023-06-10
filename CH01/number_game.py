#!/usr/bin/python
# -*- coding: utf-8 -*-
# Manao Integer (A)
# Friend Integer (B)
# Neither contain a zero
# Either reverse or divide by 10


def determineOutcome(manao_integer: int, friend_integer: int):
    if((manao_integer < 1 and manao_integer > 1000000000) or (friend_integer < 1 and friend_integer > 1000000000)):
        print("Integer should be between 1 and 999,999,999, inclusive")
        return False

    if(manao_integer == friend_integer):
        print("Integer should be distinct")
        return False

    if ((0 in [int(x) for x in str(manao_integer)]) or (0 in [int(x) for x in str(friend_integer)])):
        print("Integer will not contain a zero digit in base 10 representation")
        return False

    NUMBER_OF_MANAO_MOVES = 0
    NUMBER_OF_FRIEND_MOVES = 0
    WINNER = None
    DONE = False

    while not DONE:

        # Game instructions
        # add move if manao plays

        NUMBER_OF_MANAO_MOVES += 1

        # reverse number if manao chooses 1

        new_manao_integer_list = [int(x) for x in str(manao_integer)]
        manao_integer = ''.join(map(str,
                                list(reversed(new_manao_integer_list))))

        # check for win
        # if numbers are equal

        if manao_integer == friend_integer:
            WINNER = 'Manao'
            print('Manao Wins')
            DONE = True
        elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != 'Manao':
            WINNER = 'Friend'
            print('Manao loses')
            DONE = True

        # add move if manao plays

        NUMBER_OF_MANAO_MOVES += 1

        # divide number by 10 if manao chooses 2

        manao_integer = int(manao_integer) // 10

        # check for win
        # if numbers are equal

        if manao_integer == friend_integer:
            WINNER = 'Manao'
            print('Manao Wins')
            return True
        elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != 'Manao':
            WINNER = 'Friend'
            print('Manao loses')
            return True

        # add move if manao plays

        NUMBER_OF_FRIEND_MOVES += 1

        # reverse number if manao chooses 1

        new_friend_integer_list = [int(x) for x in str(manao_integer)]
        friend_integer = ''.join(map(str,
                                 list(reversed(new_friend_integer_list))))

        # check for win
        # if numbers are equal

        if manao_integer == friend_integer:
            WINNER = 'Manao'
            print("Manao Wins")
            return True
        elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != 'Manao':
            WINNER = 'Friend'
            print('Manao loses')
            return True

        # add move if manao plays

        NUMBER_OF_FRIEND_MOVES += 1

        # divide number by 10 if manao chooses 2

        friend_integer = int(friend_integer) // 10

        # check for win
        # if numbers are equal
        if manao_integer == friend_integer:
            WINNER = 'Manao'
            print('Manao Wins')
            return True
        elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != 'Manao':
            WINNER = 'Friend'
            print('Manao loses')
            return True


determineOutcome(900,34)