# # initialize empty array
# arr = ['1', '2', '3']
# # specify array length
# # arr_count = int(input("Enter number of array elements: ").strip())

# # populate array
# # for values in enumerate(range(0, arr_count)):
# #     arr_ele = int((input("Enter element {0}: ".format(values[0]))))
# #     arr.append(arr_ele)
# # arr = list(map(int, input("Enter a number string e.g 37648937: ").rstrip().split()))
# print("Original array: {}".format(arr))

# # reverse method 1. slicing
# # print("Reversed array: {0}".format(arr[::-1]))

# # method 1 - using the reversed() built-in function
# print("Reversed array: {0}".format(list(reversed(arr))))
# #[ele for ele in reversed(a)]


# # Manao Integer (A)
# # Friend Integer (B)
# # Neither contain a zero
# # Either reverse or divide by 10


# manao_integer = int(input("Enter integer: "))
# friend_integer = int(input("Enter integer: "))


# def reverse_integer(integer):


# def determineOutcome(manao_integer, friend_integer):
#     NUMBER_OF_MANAO_MOVES = 0
#     NUMBER_OF_FRIEND_MOVES = 0
#     WINNER = None
#     DONE = False

#     while not DONE:
#         # Game instructions
#         print("Manao's Move")
#         print("Enter 1 To reverse your number")
#         print("Enter 2 To divide your number by 10")

#         manao_choice = int(input("Choice: "))
#         if manao_choice == 1:
#             # add move if manao plays
#             NUMBER_OF_MANAO_MOVES += 1

#             # reverse number if manao chooses 1
#             new_manao_integer_list = [int(x) for x in str(manao_integer)]
#             manao_integer = ''.join(
#                 map(str, list(reversed(new_manao_integer_list))))

#             # check for win
#             # if numbers are equal
#             if manao_integer == friend_integer:
#                 WINNER = "Manao"
#                 print("Manao Wins")
#             elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != "Manao":
#                 WINNER = "Friend"
#                 print("Manao loses")

#         if manao_choice == 2:
#             # add move if manao plays
#             NUMBER_OF_MANAO_MOVES += 1

#             # divide number by 10 if manao chooses 2
#             manao_integer = manao_integer // 10

#             # check for win
#             # if numbers are equal
#             if manao_integer == friend_integer:
#                 WINNER = "Manao"
#                 print("Manao Wins")
#             elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != "Manao":
#                 WINNER = "Friend"
#                 print("Manao loses")

#         print("Friend's Move")
#         print("Enter 1 To reverse your number")
#         print("Enter 2 To divide your number by 10")

#         friend_choice = int(input("Choice: "))
#         if friend_choice == 1:
#             # add move if manao plays
#             NUMBER_OF_FRIEND_MOVES += 1

#             # reverse number if manao chooses 1
#             new_friend_integer_list = [int(x) for x in str(manao_integer)]
#             friend_integer = ''.join(
#                 map(str, list(reversed(new_friend_integer_list))))

#             # check for win
#             # if numbers are equal
#             if manao_integer == friend_integer:
#                 WINNER = "Manao"
#                 print("Manao Wins")
#             elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != "Manao":
#                 WINNER = "Friend"
#                 print("Manao loses")

#         if friend_choice == 2:
#             # add move if manao plays
#             NUMBER_OF_MANAO_MOVES += 1

#             # divide number by 10 if manao chooses 2
#             friend_integer = friend_integer // 10

#             # check for win
#             # if numbers are equal
#             if manao_integer == friend_integer:
#                 WINNER = "Manao"
#                 print("Manao Wins")
#             elif NUMBER_OF_MANAO_MOVES == 500 and NUMBER_OF_FRIEND_MOVES == 500 and WINNER != "Manao":
#                 WINNER = "Friend"
#                 print("Manao loses")

if ((0 in [int(x) for x in str(234450)])):
    print("Integer will not contain a zero digit in base 10 representation")
