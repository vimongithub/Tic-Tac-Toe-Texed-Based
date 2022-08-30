print("Welcome to Tic-Tac-Toe\n")
print("======> Player 1 = 'X' <======")
print("======> Player 2 = 'O' <====== \n\n")


place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
store_number = []
zero = 0
player_1 = True
game_on = True


def game_board():
    game = f'{place[0]}  |  {place[1]}  |  {place[2]} \n' \
           f'-------------\n' \
           f'{place[3]}  |  {place[4]}  |  {place[5]} \n' \
           f'-------------\n' \
           f'{place[6]}  |  {place[7]}  |  {place[8]} \n\n'

    print(game)


game_board()

def winning_scenario():

    if place[0] == place[1] == place[2] or place[3] == place[4] == place[5] or \
            place[6] == place[7] == place[8] or place[0] == place[3] == place[6] or \
            place[1] == place[4] == place[7] or place[2] == place[5] == place[8] or \
            place[0] == place[4] == place[8] or place[6] == place[4] == place[2]:

        return True


def game_start():
    global place, store_number, game_on, player_1

    while game_on:
        try:
            if player_1:
                user_input = int(input("\n  >> Player 'X', Where you want to put 'X' (1 to 9) :: "))
                print('\n')
                zero_detect = 1 / user_input

                if user_input < 0:
                    raise ValueError
                else:
                    user_input -= 1

                if user_input in store_number:
                    print(f"\n ==> Number {user_input + 1} box already filled by 'Player 2 (O)' <==\n")

                else:
                    store_number.append(user_input)
                    place[user_input] = 'X'
                    game_board()
                    player_1 = False

            else:
                user_input = int(input("\n  >> Player 'O', Where you want to put 'O' (1 to 9) :: "))
                print('\n')
                zero_detect = 1 / user_input

                if user_input < 0:
                    raise ValueError
                else:
                    user_input -= 1

                if user_input in store_number:
                    print(f"\n ==> Number {user_input + 1} box already filled by 'Player 1 (X)' <==")

                else:
                    store_number.append(user_input)
                    place[user_input] = 'O'
                    game_board()
                    player_1 = True

        except ValueError:
            print("\n ==> Please, Enter number between 1 to 9 <==")
            game_board()

        except IndexError:
            print("\n ==> Please, Enter number between 1 to 9 <==")
            game_board()

        except ZeroDivisionError:
            print("\n ==> Please, Enter number between 1 to 9 <==")
            game_board()

        if winning_scenario():
            if player_1:
                print("\n==> ** Player 2('O') won the game ** <==")
                game_on = False
            else:
                print("\n==> ** Player 1('X') won the game ** <==")
                game_on = False

        elif len(store_number) == 9:
            print("==> ** The game is draw ** <==")
            game_on = False


user_choice = input(" --> Type '1' to Start the game :: type '0' to Exit:  ")
if user_choice == "1":
    game_start()
else:
    exit()
