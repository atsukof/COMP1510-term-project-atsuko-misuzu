import time


def make_a_board():
    """
    Make a game board.

    :return:
    """
    board_dict = {}
    rows = 10
    columns = 10

    for row in range(rows):
        for column in range(columns):
            board_tuple = (row, column)
            board_dict[board_tuple] = "Random Street"

    # special locations
    board_dict[(4,0)] = "Kyoto Station"
    board_dict[(0,9)] = "Kinkakuji Temple"
    board_dict[(8,3)] = "Kiyomizudera Temple"
    board_dict[(3,3)] = "Nishiki Market"
    board_dict[(4,3)] = "Nishiki Market"
    board_dict[(2,4)] = "Nijojo Castle"
    board_dict[(4,4)] = "Ueshima Coffee"
    board_dict[(3,6)] = "Kyoto Imperial Palace"
    board_dict[(7,7)] = "Kyoto University"

    print(board_dict)

    return board_dict


def make_character():
    """

    :return:
    """
    character_dict = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'KEP': 0}
    while True:
        user_name = input('Enter your name: ')
        user_response = input(f'Are you okay with {user_name}? type "y" for yes, "n" for no: ')
        if user_response.lower() == 'n':
            continue
        elif user_response.lower() == 'y':
            print(f'Hello {user_name}, let\'s explore Kyoto with us!')
            break
        while user_response.lower() != 'y' and user_response.lower() != 'n':
            user_response = input(f'Are you okay with {user_name}? type "y" for yes, "n" for no: ')

    character_dict['Name'] = user_name
    return character_dict


def instruction():
    """
    Print instruction of the game.

    """
    time.sleep(1)
    print('Through this game, you can explore Kyoto which is one of our most favourite cities.')
    time.sleep(2)
    print('Your mission is to go to Kinkakuji temple, and defeat a monk.')
    time.sleep(2)
    print('''To fight with a monk, answer random quizzes correctly to earn Kyoto Experience Points(KEP). 
    The quizzes are about Japan.''')
    time.sleep(3)
    print('''If you answer incorrectly, your HP will decrease by 1. 
    Before your HP becomes 0, you need to find food and eat.''')
    time.sleep(3)
    print('Let\'s begin!')
    time.sleep(1)


def show_status_and_map(user_character, board):
    """
    Print user's current location in map and character.
    :param user_character:
    :param board:
    :precondition:
    :postcondition:
    """
    map_string = """
    !─~─~─~─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─~─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─~─~─~─~─!─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─!─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─~─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─!─~─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─!!!─~─~─~─!─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─~─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─~─~─~─~─~─~─~
    │ │ │ │ │ │ │ │ │ │
    ~─~─~─~─!─~─~─~─~─~
    """
    print(map_string)
    print(board)
    print(user_character)


def get_user_choice():
    """
    Ask users to enter the direction they wish to travel and return the users' choice.

    Print a numbered list of directions options.

    :precondition: player's HP is greater than zero
    :postcondition: the function let users enter a number until they enter a correct number
    :return: an integer between 1 and 4 inclusive
    """
    while True:
        user_choice_list = ['1', '2', '3', '4']
        user_choice = input(f'Which direction do you want to go? '
                            f'Type 1 for North, 2 for East, 3 for South, and 4 for West\n {user_choice_list} \n')
        if user_choice in user_choice_list:
            return int(user_choice)
        print('You need to choose from the list!')


def validate_direction(board, character, direction):
    """
    Validate if the character's move is on the board.

    Check whether the character can travel in their desired direction.

    :param board: a dictionary that contains rows * columns keys and a short description
    :param character: a dictionary that contains X- and Y-coordinates and current status
    :param direction: an integer of direction users have chosen
    :precondition: a board must be a dictionary that contains rows * columns keys and a short description
    :precondition: a character must be a dictionary that contains coordinate and current HP
    :precondition: a direction must be an integer between 1 and 4 inclusive
    :postcondition: check if the move is valid, return True if it is, else False
    :return: a Boolean
    """
    is_valid = False
    direction_dictionary = {}
    move = direction_dictionary[direction]
    next_location = (character['X-coordinate'] + move[0], character['Y-coordinate'] + move[1])
    if next_location in board.keys():
        is_valid = True
    return is_valid


def move_user(character, direction):
    """

    """
    pass


def is_kinkakuji():
    """

    :return:
    """
    pass


def check_quiz():
    """

    :return:
    """
    pass


def play_quiz():
    """

    :return:
    """
    pass


def check_level_up():
    """

    :return:
    """
    pass


def is_achieved_level_3():
    """

    :return:
    """
    pass


def is_food_station(character, board):
    """

    :param character:
    :param board:
    :precondition:
    :postcondition:
    :return:
    """
    is_food = False
    current_location = board[(character['X-coordinate'], character['Y-coordinate'])]
    if current_location != 'Random Street' and current_location != 'Kinkakuji Temple':
        is_food = True
    return is_food


def eat_food(character):
    """

    :param character:
    :precondition:
    :return:
    """
    food_choice = input('Do you want to eat food here? type "y" for yes, "n" for no: ')
    if food_choice.lower() == 'y':
        character['Current HP'] += 1
        print('Oishii! Your Current HP was increased by 1')
    else:
        print('You did\'t eat anything here.')


def fight_with_monk():
    """

    """
    pass


def lose_monk():
    """

    :return:
    """
    pass


def is_alive(user_character):
    """

    :return:
    """
    alive = user_character['Current HP'] > 0
    return alive


def game():
    """
    Run the game.
    """
    board = make_a_board()
    character = make_character()
    instruction()
    show_status_and_map(character, board)

    while is_alive(character):
        direction = get_user_choice()
        valid_move = validate_direction(board, character, direction)
        if valid_move:
            move_user(character, direction)
            show_status_and_map(character, board)
        else:
            # Tell the users they cannot go in that direction
            print('Oops! You cannot go this direction.')
            show_status_and_map(character, board)

    eat_food(character)





def main():
    # make_a_board()
    # show_status_and_map()
    game()



if __name__ == '__main__':
    main()
