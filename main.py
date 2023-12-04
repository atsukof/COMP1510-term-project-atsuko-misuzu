import time
import random
import json


def make_board():
    """
    Create a 10 x 10 game board.

    Each point on the game board is represented by coordinates ranging from (0, 0) to (9, 9),
    and each point is assigned a name.
    Special locations on the board have specific coordinates, while others are named "Random Street."
    :postcondition: creates a 10 x 10 game board
    :return: a dictionary where keys are coordinates and values are names of the places

    >>> make_board()
    {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    """
    board_dict = {}
    rows = 10
    columns = 10

    for row in range(rows):
        for column in range(columns):
            board_tuple = (row, column)
            board_dict[board_tuple] = "Random Street"

    filename = "special_location.json"
    with open(filename) as file_object:
        special_location_list = json.load(file_object)

    for location in special_location_list:
        location_tuple = location["x_coordinate"], location["y_coordinate"]
        board_dict[location_tuple] = location["name"]

    return board_dict


def make_level_dict():
    level_dict = {
        "level 1": {"KEP_min": 0, "KEP_max": 2, "maximum_HP": 5, "name": "Kyoto rookie"},
        "level 2": {"KEP_min": 3, "KEP_max": 5, "maximum_HP": 7, "name": "Kyoto skilled novice"},
        "level 3": {"KEP_min": 6, "KEP_max": 9999, "maximum_HP": 10, "name": "Kyoto expert"},
    }
    return level_dict


def make_character():
    """
    Create a dictionary with character's information.

    This function allows a user to enter character's name.
    After the character's name is determined, this function returns a dictionary with character's information.
    :postcondition: creates a dictionary with character's information
    :return: a dictionary where keys are X- Y-coordinates, Current HP, KEP, and name of the character
    """
    character_dict = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0}
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

    :postcondition: prints instruction of the game
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


def show_status_and_map(character, board):
    """
    Print user's current location in map and character.

    :param character: a dictionary where keys are X- Y-coordinates, Current HP, KEP, and name of the character
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: character must conform to the format specified in the parameter
    :postcondition: board must be a dictionary with keys and values described in param board
    """
    print("\n[Map]")
    for y_coordinate in range(10):
        for x_coordinate in range(10):
            if (x_coordinate, y_coordinate) == (character['X-coordinate'], character['Y-coordinate']):
                print("■■", end="")
            elif board[(x_coordinate, y_coordinate)] == "Random Street":
                print("△△", end="")
            elif board[(x_coordinate, y_coordinate)] == "Kinkakuji Temple":
                print("★★", end="")
            else:
                print("##", end="")
        print()
    print("\nGoal(Kinkakuji Temple) is ★★.")

    user_status = (f"\n[Your status]"
                   f"\nName: {character['Name']}"
                   f"\nCurrent HP: {character['Current HP']}\n"
                   f"KEP: {character['KEP']}\n"
                   f"Location:({character['X-coordinate']}, {character['Y-coordinate']}) *plotted with ■■")

    time.sleep(1)
    print(user_status)


def get_user_choice():
    """
    Ask a user to enter the direction they wish to travel and return the user's choice.

    This function prompts the user to input an integer between 1 and 4 (inclusive).
    If the user enters something other than an integer, the function requests input again.
    :postcondition: the function let a user enter a number until they enter a correct number
    :return: an integer between 1 and 4 inclusive
    """
    while True:
        user_choice_list = ['1', '2', '3', '4']
        user_choice = input(f'\nWhich direction do you want to go? Enter your choice from 1-4.\n'
                            f'1 North (↑)\n2 East (→)\n3 South (↓)\n4 West (←)\n'
                            f'Your choice [1, 2, 3, 4]: ')
        if user_choice in user_choice_list:
            return int(user_choice)
        print('You need to choose from the list!')


def validate_direction(board, character, direction):
    """
    Validate if the character can move to the specified direction.

    :param board: a dictionary where keys are coordinates and values are names of the places
    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param direction: an integer of direction users have chosen
    :precondition: board must be a dictionary that contains rows * columns keys and a short description
    :precondition: character must be a dictionary that contains coordinate, current status, and name
    :precondition: direction must be an integer between 1 and 4 inclusive
    :postcondition: check if the move is valid, return True if it is, else False
    :return: a Boolean

    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> user_character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris'}
    >>> validate_direction(user_board, user_character, 3)
    False
    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> user_character = {'X-coordinate': 4, 'Y-coordinate': 7, 'Current HP': 4, 'KEP': 1, 'Name': 'Chris'}
    >>> validate_direction(user_board, user_character, 4)
    True
    """
    is_valid = False
    direction_dictionary = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
    move = direction_dictionary[direction]
    next_location = (character['X-coordinate'] + move[0], character['Y-coordinate'] + move[1])
    if next_location in board.keys():
        is_valid = True
    return is_valid


def move_user(character, direction):
    """
    Update character's X- and Y-coordinates depending on the direction selected by the user.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param direction: an integer between 1 and 4 inclusive
    :precondition: character must be a dictionary that contains coordinate, current status, and name
    :precondition: direction must be an integer between 1 and 4 inclusive
    :postcondition: updates character's X- and Y-coordinates depending on the direction selected by the user

    >>> user_character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris'}
    >>> move_user(user_character, 1)
    >>> user_character
    {'X-coordinate': 4, 'Y-coordinate': 8, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris'}
    >>> user_character = {'X-coordinate': 3, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 1, 'Name': 'Chris'}
    >>> move_user(user_character, 4)
    >>> user_character
    {'X-coordinate': 2, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 1, 'Name': 'Chris'}
    """
    direction_dictionary = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
    move = direction_dictionary[direction]

    character["X-coordinate"] += move[0]
    character["Y-coordinate"] += move[1]


def is_kinkakuji(character, board):
    """
    Check if the character has reached the goal.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: character must conform to the format specified in the parameter
    :precondition: board must conform to the format specified in the parameter
    :postcondition: checks if the character is in the goal
    :return: a Boolean

    >>> user_character = {'X-coordinate': 5, 'Y-coordinate': 6, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris'}
    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> is_kinkakuji(user_character, user_board)
    False
    >>> user_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 3, 'KEP': 7, 'Name': 'Chris'}
    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> is_kinkakuji(user_character, user_board)
    True
    """
    kinkakuji = False
    current_location = board[(character['X-coordinate'], character['Y-coordinate'])]
    if current_location == 'Kinkakuji Temple':
        kinkakuji = True
    return kinkakuji


def check_quiz():
    """
    Return True with 30% of chance.

    This function generates a random number between 1 and 10 inclusive.
    If the random number is equal or less than 3, the function returns True.
    :postcondition: generates a random number between 1 and 10 inclusive
    :postcondition: returns True if the random number is equal or less than 3, else False
    :return: a Boolean
    """
    encounter_quiz = random.randint(1, 10)
    return encounter_quiz <= 3


def play_quiz(character):
    """
    Print random quiz.

    Increase KEP by 1 if user choose the correct choice, decrease Current HP if they choose wrong one.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: print random quiz
    :postcondition: increase KEP by 1 if user choose the correct choice, decrease Current HP if they choose wrong one
    """
    filename = "quiz.json"
    with open(filename) as file_object:
        quiz_list = json.load(file_object)

    random_number = random.randint(0, 11)
    print(quiz_list[random_number]["quiz"])
    options = (f"1. {quiz_list[random_number]['1']}\n"
               f"2. {quiz_list[random_number]['2']}\n"
               f"3. {quiz_list[random_number]['3']}\n"
               f"4. {quiz_list[random_number]['4']}")
    print(options)
    time.sleep(1)

    user_answer = input("Enter your answer with a number:")

    if user_answer == quiz_list[random_number]["ans"]:
        print("You are correct, your KEP was increased by 1")
        character["KEP"] += 1
    else:
        print("You are wrong, your HP was decreased by 1")
        character["Current HP"] -= 1
    time.sleep(1)


def check_level_up(character, level_dictionary):
    """
    Check the user's current level based on KEP and print it.

    Print if the user's level has increased.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param level_dictionary: a dictionary #あとで書く
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: check the user's current level based on KEP and print it
    """
    time.sleep(1)
    current_kep = character['KEP']
    if current_kep <= level_dictionary["level 1"]["KEP_max"]:
        print(f'Now you are {level_dictionary["level 1"]["name"]} (level 1).')
    elif current_kep <= level_dictionary["level 2"]["KEP_max"]:
        print(f'Now you are {level_dictionary["level 2"]["name"]} (level 2).')
    else:
        print(f'You are {level_dictionary["level 3"]["name"]} (level 3) now! '
              f'You\'re ready to fight with monk at Kinkakuji Temple.')


def is_achieved_level_3(character):
    """
    Check if the character reach level 3

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: return True if the character reach level 3, else False
    :return: a Boolean

    >>> user_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 3, 'KEP': 7, 'Name': 'Chris'}
    >>> is_achieved_level_3(user_character)
    True
    >>> user_character = {'X-coordinate': 5, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 2, 'Name': 'Chris'}
    >>> is_achieved_level_3(user_character)
    False
    """
    current_level = character['KEP'] >= 6
    return current_level


def is_food_station(character, board):
    """
    Check if the character has reached the food station.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :precondition: board must conform to the format specified in the parameter
    :postcondition: return True if the character has reached the food station, else False
    :return: a Boolean
    """
    filename = "special_location.json"
    with open(filename) as file_object:
        special_location_list = json.load(file_object)

    is_food = False
    current_location = board[(character['X-coordinate'], character['Y-coordinate'])]
    for location in special_location_list:
        if current_location == location["name"] and current_location != 'Kinkakuji Temple':
            is_food = True
            print(f'Here is {current_location}. \n{location["explanation"]}You can eat {location["food"]} here.')

    return is_food


def eat_food(character):
    """
    Increase the Current HP by eating food if user want to.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: increase the Current HP by eating food if user want to
    """
    food_choice = input('Do you want to eat food here? type "y" for yes, "n" for no: ')
    if food_choice.lower() == 'y':
        character['Current HP'] += 1
        time.sleep(1)
        print('Oishii! Your Current HP was increased by 1')
    else:
        print('You did\'t eat anything here.')
    time.sleep(1)


def fight_with_monk():
    """
    Get user input and compare it with the number that is randomly generated.

    Play rock-paper-scissors game.

    :postcondition: return True if user wins the rock-paper-scissors game, else False
    :return: a Boolean
    """
    monk_pic = """
                         ..(gmQa-,
                   .M"`      (TQ,
                  d3            Ux
        `        J%              H,        `   `
    `     `  `   #    ..    ..   -]  `  `
       `       ..M          `    -N,         `
              .M`     NF `  NF     ?b      `    `
   `    `  `   N,.,      ,.    ` ...F   `
      `         ?Tb             .M"!         `
                  ?m.   777^   .M'         `    `
   `     `   `  .xMmWa,    `..dNMNJ.   `
      `   `  .J@!  ,H,.WM"WM=.M^  .#N,  `   `  `
            .@`      ?N,,MD.M=   JD (Mm.
    `      (D         .M"M@H, .M""NM^ ,N.
       `  (F          g% M~.N.dL  g\   ,N.  `  `
   `     .F   ..     .F  M~ ,M$?M"' ,   Jb
      ` .M`   J]  `..#   M~  qNM'  .#    Wc  `
        Jt    J] .J@M\   M~   MTN, .#    .N.    `
   `   .#     Jhd"  Me  .MN, .M. ?HJ#     Jb
       d'    .#=   .MMMM]M?MMMMN   .Ta, `  M.  `
      .F    "!    .MMMMM`M;HMMMMb     T^   -b
    """
    print(monk_pic)
    print('Monk wants to fight with you. Let\'s play rock-paper-scissors game!')
    user_won = False

    while True:
        choice_dictionary = {1: 'rock', 2: 'paper', 3: 'scissors'}
        monk_choice = random.randint(1, 3)
        user_choice_option_list = ['1', '2', '3']
        user_choice = input(f'Which do you want to choose? Type 1 for rock, 2 for paper, 3 for scissors.\n'
                            f'Your choice {user_choice_option_list}: ')
        if user_choice not in user_choice_option_list:
            print(f'You should choose from {user_choice_option_list}!')
            continue

        int_user_choice = int(user_choice)
        print(f'You threw {choice_dictionary[int_user_choice]}, and the monk threw {choice_dictionary[monk_choice]}!')
        if monk_choice == user_choice:
            print('Draw! Try one more time.')
            time.sleep(1)
            continue
        elif monk_choice < int_user_choice:
            if monk_choice == 1 and int_user_choice == 3:
                break
            else:
                user_won = True
                break
        else:
            if monk_choice == 3 and int_user_choice == 1:
                user_won = True
                break
            else:
                break

    if user_won:
        print('Hooray, you won!')
    else:
        print('Oh no, you lost!')
    time.sleep(2)
    return user_won


def lose_monk(character):
    """
    Decrease character's Current HP by 2.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: decrease character's Current HP by 2.

    >>> user_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4, 'KEP': 8, 'Name': 'Chris'}
    >>> lose_monk(user_character)
    >>> user_character
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 2, 'KEP': 8, 'Name': 'Chris'}
    >>> user_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 2, 'KEP': 7, 'Name': 'Chris'}
    >>> lose_monk(user_character)
    >>> user_character
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 0, 'KEP': 7, 'Name': 'Chris'}

    """
    character['Current HP'] -= 2


def is_alive(character):
    """
    Check if character's Current HP reaches zero or not.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: user_character must contain X- and Y-coordinates, current status, and name
    :postcondition: check if the current HP in character reaches zero or not
    :return: a Boolean

    >>> user_character = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 3, 'KEP': 5, 'Name': 'Chris'}
    >>> is_alive(user_character)
    True
    >>> user_character = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 0, 'KEP': 3, 'Name': 'Chris'}
    >>> is_alive(user_character)
    False
    """
    alive = character['Current HP'] > 0
    return alive


def game():
    """
    Run the game.
    """
    board = make_board()
    character = make_character()
    instruction()
    level_dictionary = make_level_dict()

    complete = False
    while is_alive(character) and not complete:
        show_status_and_map(character, board)
        check_level_up(character, level_dictionary)
        direction = get_user_choice()
        valid_move = validate_direction(board, character, direction)
        if valid_move:
            move_user(character, direction)

            if is_food_station(character, board):
                eat_food(character)

            kinkakuji = is_kinkakuji(character, board)
            level_3 = is_achieved_level_3(character)
            if kinkakuji and level_3:
                complete = fight_with_monk()
                if not complete:
                    lose_monk(character)
            elif kinkakuji and not level_3:
                print('Your level is not high enough to fight with monk! Walk around Kyoto to get KEP.')
            else:
                quiz = check_quiz()
                if quiz:
                    play_quiz(character)
        else:
            print('Oops! You cannot go this direction.')

    if not is_alive(character):
        print("Your HP reached 0. Game over....")
    else:
        print("You complete the game!\n Now you are a master of Kyoto!")
        time.sleep(1)
        message = """                                                 
          ___   __    __  _    __   ___    __    _____   _  _   _      __    _____   _    __    __  _    __  
         / _/  /__\  |  \| |  / _] | _ \  /  \  |_   _| | || | | |    /  \  |_   _| | |  /__\  |  \| | /' _/ 
        | \__ | \/ | | | ' | | [/\ | v / | /\ |   | |   | \/ | | |_  | /\ |   | |   | | | \/ | | | ' | `._`. 
         \__/  \__/  |_|\__|  \__/ |_|_\ |_||_|   |_|    \__/  |___| |_||_|   |_|   |_|  \__/  |_|\__| |___/ 
        """
        print(message)


def main():
    board = make_board()
    character = make_character()
    level_dictionary = make_level_dict()

    # game()
    # fight_with_monk()
    check_level_up(character, level_dictionary)


if __name__ == '__main__':
    main()
