import time
import random
import json
from itertools import combinations


def make_board() -> dict:
    """
    Create a 10 x 10 game board.

    Each point on the game board is represented by coordinates ranging from (0, 0) to (9, 9),
    and each point is assigned a name.
    Special locations on the board have specific coordinates, while others are named "Random Street."

    :postcondition: creates a 10 x 10 game board
    :return: a dictionary where keys are coordinates and values are names of the places

    >>> make_board()
    {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Random Street', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    """
    rows = 10
    columns = 10
    board_dict = {(row, column): "Random Street" for row in range(rows) for column in range(columns)}

    filename = "special_location.json"
    with open(filename) as file_object:
        special_location_list = json.load(file_object)

    for location in special_location_list:
        location_tuple = location["x_coordinate"], location["y_coordinate"]
        board_dict[location_tuple] = location["name"]

    return board_dict


def make_level_dict() -> dict:
    """
    Create a dictionary that contains levels and their explanation.

    :postcondition: create a dictionary that contains levels and their explanation
    :return: a dictionry that contains levels and their explanation

    >>> make_level_dict()
    {'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'}, 'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'}, 'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}}
    """
    level_dict = {
        "level 1": {"KEP_max": 2, "maximum_HP": 5, "name": "Kyoto rookie"},
        "level 2": {"KEP_max": 5, "maximum_HP": 7, "name": "Kyoto skilled novice"},
        "level 3": {"KEP_max": 9999, "maximum_HP": 10, "name": "Kyoto expert"},
    }
    return level_dict


def make_character() -> dict:
    """
    Create a dictionary with character's information.

    This function allows a user to enter character's name.
    After the character's name is determined, this function returns a dictionary with character's information.

    :postcondition: creates a dictionary with character's information
    :return: a dictionary where keys are X- Y-coordinates, Current HP, KEP, and name of the character
    """
    character_dict = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1'}
    while True:
        user_name = input('Enter your name: ')
        user_response = input(f'Are you okay with {user_name}? type "y" for yes, "n" for no: ')
        if user_response.lower() == 'n':
            continue
        elif user_response.lower() == 'y':
            print(f'Hello {user_name}, let\'s explore Kyoto with us!')
            break
        else:
            print('Your input is not valid, try again.')

    character_dict['Name'] = user_name
    return character_dict


def instruction() -> None:
    """
    Print instruction of the game.

    :postcondition: prints instruction of the game
    """
    time.sleep(1)
    print('Through this game, you can explore Kyoto which is one of our most favourite cities.')
    time.sleep(2)
    print('Your mission is to go to Kinkakuji temple, and defeat a monk.')
    time.sleep(2)
    print('To fight with a monk, answer random quizzes correctly to earn Kyoto Experience Points(KEP).'
          'The quizzes are about Japan.')
    time.sleep(3)
    print('If you answer incorrectly, your HP will decrease by 1.'
          'Before your HP becomes 0, you need to find food and eat.')
    time.sleep(3)
    print('Let\'s begin!')
    time.sleep(1)


def show_status_and_map(character: dict, board: dict) -> None:
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

    user_status = (f"\n[Your status]\n"
                   f"Name: {character['Name']}\n"
                   f"Current HP: {character['Current HP']}\n"
                   f"KEP: {character['KEP']}\n"
                   f"Level: {character['Level']}\n"
                   f"Location:({character['X-coordinate']}, {character['Y-coordinate']}) *plotted with ■■")

    time.sleep(1)
    print(user_status)


def get_user_choice() -> int:
    """
    Ask a user to enter the direction they wish to travel and return the user's choice.

    This function prompts the user to input an integer between 1 and 4 inclusive.
    If the user enters something other than an integer between 1 and 4, the function requests input again.

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


def validate_direction(board: dict, character: dict, direction: int) -> bool:
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
    >>> user_character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris', 'Level': 'level 1'}
    >>> validate_direction(user_board, user_character, 3)
    False
    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> user_character = {'X-coordinate': 4, 'Y-coordinate': 7, 'Current HP': 4, 'KEP': 1, 'Name': 'Chris', 'Level': 'level 1'}
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


def move_user(character: dict, direction: int) -> None:
    """
    Update character's X- and Y-coordinates depending on the direction selected by the user.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param direction: an integer between 1 and 4 inclusive
    :precondition: character must be a dictionary that contains coordinate, current status, and name
    :precondition: direction must be an integer between 1 and 4 inclusive
    :postcondition: updates character's X- and Y-coordinates depending on the direction selected by the user

    >>> user_character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris',  'Level': 'level 1'}
    >>> move_user(user_character, 1)
    >>> user_character
    {'X-coordinate': 4, 'Y-coordinate': 8, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris'}
    >>> user_character = {'X-coordinate': 3, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 1, 'Name': 'Chris',  'Level': 'level 1'}
    >>> move_user(user_character, 4)
    >>> user_character
    {'X-coordinate': 2, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 1, 'Name': 'Chris'}
    """
    direction_dictionary = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
    move = direction_dictionary[direction]

    character["X-coordinate"] += move[0]
    character["Y-coordinate"] += move[1]


def is_kinkakuji(character: dict, board: dict) -> bool:
    """
    Check if the character has reached the goal point.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: character must conform to the format specified in the parameter
    :precondition: board must conform to the format specified in the parameter
    :postcondition: checks if the character is in the goal point
    :return: a Boolean

    >>> user_character = {'X-coordinate': 5, 'Y-coordinate': 6, 'Current HP': 5, 'KEP': 0, 'Name': 'Chris', 'Level': 'level 1'}
    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> is_kinkakuji(user_character, user_board)
    False
    >>> user_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 3, 'KEP': 7, 'Name': 'Chris',  'Level': 'level 3'}
    >>> user_board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street', (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street', (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street', (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street', (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street', (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street', (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street', (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street', (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace', (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market', (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street', (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street', (4, 5): 'Ueshima Coffee', (4, 6): 'Nishiki Market', (4, 7): 'Random Street', (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street', (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street', (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street', (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street', (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street', (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street', (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street', (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street', (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street', (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street', (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street', (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street', (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street', (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
    >>> is_kinkakuji(user_character, user_board)
    True
    """
    kinkakuji = False
    current_location = board[(character['X-coordinate'], character['Y-coordinate'])]
    if current_location == 'Kinkakuji Temple':
        kinkakuji = True
    return kinkakuji


def check_quiz() -> bool:
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


def get_random_quiz():
    """
    Get a random quiz from quiz.json.

    The function opens quiz.json and loads the data as a list of quiz dictionaries.
    It generates a random number and returns a quiz dictionary based on the number.
    :postcondition: gets a random quiz from quiz.json
    :return: a dictionary which contains question, options 1-4, and answer as keys.
    """
    filename = "quiz.json"
    with open(filename) as file_object:
        quiz_list = json.load(file_object)

    random_number = random.randint(0, 11)
    random_quiz = quiz_list[random_number]
    return random_quiz


def print_quiz(quiz_dictionary):
    """
    Print a quiz question and options.

    :param quiz_dictionary: a dictionary which contains question, options 1-4, and answer as keys.
    :precondition: quiz_dictionary must be a dictionary which contains question, options 1-4, and answer as keys.
    :postcondition: prints a quiz question and options.
    :return: prints a quiz question and options.
    """
    print(quiz_dictionary["quiz"])
    print(f"1. {quiz_dictionary['1']}\n"
          f"2. {quiz_dictionary['2']}\n"
          f"3. {quiz_dictionary['3']}\n"
          f"4. {quiz_dictionary['4']}")
    time.sleep(1)


def play_quiz(character: dict) -> None:
    """
    Allow users to play quiz.

    The function increases KEP by 1 if users choose the correct answer,
    decreases Current HP if users choose wrong answer.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: prints a random quiz
    :postcondition: increases KEP by 1 if user chooses the correct answer
    :postcondition: decreases Current HP by 1 if the user chooses wrong answer
    """
    quiz_dict = get_random_quiz()
    print_quiz(quiz_dict)

    while True:
        user_answer = input("Enter your answer with a number ['1', '2', '3', '4']:")
        if user_answer == quiz_dict["ans"]:
            print("You are correct, your KEP was increased by 1")
            character["KEP"] += 1
            break
        elif user_answer in ['1', '2', '3', '4']:
            print("You are wrong, your HP was decreased by 1")
            character["Current HP"] -= 1
            break
        else:
            print('Something is wrong... Enter your answer again.')
        time.sleep(1)


def check_level(character: dict, level_dictionary: dict) -> None:
    """
    Check the user's current level based on KEP and print it.

    Print if the user's level has increased.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param level_dictionary: a dictionry that contains levels and their explanation
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: checks the user's current level based on KEP and prints it

    >>> my_character = {'Name': 'Atsuko', 'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1'}
    >>> level_dict = {'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'}, 'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'}, 'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}}
    >>> check_level(my_character, level_dict)
    Now you are Kyoto rookie (level 1).
    >>> my_character
    {'Name': 'Atsuko', 'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1'}

    >>> your_character = {'Name': 'Misuzu', 'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 6, 'Level': 'level 2'}
    >>> level_dict_2 = {'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'}, 'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'}, 'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}}
    >>> check_level(your_character, level_dict)
    You are Kyoto expert (level 3) now! You're ready to fight with monk at Kinkakuji Temple.
    >>> your_character
    {'Name': 'Misuzu', 'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 6, 'Level': 'level 3'}
    """
    time.sleep(1)
    current_kep = character['KEP']
    if current_kep <= level_dictionary["level 1"]["KEP_max"]:
        print(f'Now you are {level_dictionary["level 1"]["name"]} (level 1).')
    elif current_kep <= level_dictionary["level 2"]["KEP_max"]:
        character["Level"] = "level 2"
        print(f'Now you are {level_dictionary["level 2"]["name"]} (level 2).')
    else:
        character["Level"] = "level 3"
        print(f'You are {level_dictionary["level 3"]["name"]} (level 3) now! '
              f'You\'re ready to fight with monk at Kinkakuji Temple.')


def is_achieved_level_3(character: dict) -> bool:
    """
    Check if the character reach level 3

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: returns True if the character reach level 3, else False
    :return: a Boolean

    >>> user_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 3, 'KEP': 7, 'Name': 'Chris',  'Level': 'level 3'}
    >>> is_achieved_level_3(user_character)
    True
    >>> user_character = {'X-coordinate': 5, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 2, 'Name': 'Chris',  'Level': 'level 1'}
    >>> is_achieved_level_3(user_character)
    False
    """
    current_level = character['KEP'] >= 6
    return current_level


def is_food_station(character: dict, board: dict) -> bool:
    """
    Check if the character has reached the food station.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :precondition: board must conform to the format specified in the parameter
    :postcondition: returns True if the character has reached the food station, else False
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


def eat_food(character: dict, level_dictionary: dict) -> None:
    """
    Increase the Current HP by eating food if user wants to.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param level_dictionary: a dictionary that contains levels and their explanation
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: increases the Current HP by eating food if user wants to
    """
    user_level = character["Level"]
    max_hp = level_dictionary[user_level]["maximum_HP"]
    user_hp = character["Current HP"]

    while True:
        food_choice = input('Do you want to eat food here? type "y" for yes, "n" for no: ')
        if food_choice.lower() == 'y':
            if user_hp < max_hp:
                character['Current HP'] += 1
                time.sleep(1)
                print('Oishii! Your Current HP was increased by 1')
            else:
                print('You are full. Your HP is maximum. You could not eat the food.')
            break
        elif food_choice.lower() == 'n':
            print('You did\'t eat anything here.')
            break
        else:
            print('You can only type "y" or "n". Try again.')
    time.sleep(1)


def print_monk_pic() -> None:
    """
    Print a monk's picture with a simple ASCII art.

    :postcondition: prints a monk's picture with a simple ASCII art
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


def decide_monk_choice(cards) -> set:
    """
    Determine the monk's choice from the possible combinations of the cards.

    :param cards: a dictionary which contains cards
    :precondition: cards must be a dictionary which contains cards information as value
    :postcondition: determine the monk's card choice
    :return: a set
    """
    combination_list = []
    for first, second in combinations(cards, 2):
        card_set = {first, second}
        combination_list.append(card_set)

    monk_choice_number = random.randint(0, 5)
    combination_set = combination_list[monk_choice_number]
    return combination_set


def monk_game_instruction() -> None:
    """
    Print instruction of the game with monk.

    :postcondition: print instruction of the game with monk
    """
    time.sleep(1)
    print('The monk has challenged you to a game! It\'s a game using Hanafuda(花札), a traditional Japanese card game.\n'
          'Out of four beautifully illustrated cards, the monk selects two.\n')
    time.sleep(2)
    print('Your task is to guess which cards the monk is holding.\n'
          'The four cards feature drawings of 1. boar(猪), 2. deer(鹿), 3. butterfly(蝶), and 4. crane(鶴).\n')
    time.sleep(2)
    print('Choose two of them and provide your answer one by one (the order does not matter).')


def get_user_combination() -> list:
    """
    Get two user choices and put into a list.

    :postcondition: get two user choices
    :return: a list of user's choice
    """
    while True:
        try:
            first_card = int(input('Choose your 1st card from 1-4: '))
            second_card = int(input('Choose your 2nd card from 1-4: '))
        except ValueError:
            print('You can only input numbers in 1-4. Try again.')
        else:
            if first_card not in [1, 2, 3, 4] or second_card not in [1, 2, 3, 4]:
                print('You can only input numbers in 1-4. Try again.')
            else:
                break

    user_choice = [first_card, second_card]
    return user_choice


def fight_with_monk() -> bool:
    """
    Play game with the monk.

    The function generates a set with random two integers in 1-4 using combinations method called as monk_choice.
    It gets user input of two integers, and makes a set of them called as user_choice.
    It compares monk_choice and user_choice.
    If the two sets are identical, the function returns True. If not, the function returns False.

    :postcondition: returns True if user wins the rock-paper-scissors game, else False
    :return: a Boolean
    """
    cards = {1: 'boar', 2: 'deer', 3: 'butterfly', 4: 'crane'}
    monk_choice = decide_monk_choice(cards)
    monk_game_instruction()
    user_choice_list = get_user_combination()

    if monk_choice == set(user_choice_list):
        print('Hooray, you won!')
        user_won = True
    else:
        print('Oh no, you lost!')
        user_won = False

    print(f'The monk is holding "{cards[monk_choice.pop()]}" and "{cards[monk_choice.pop()]}".')
    print(f'You choose "{cards[user_choice_list[0]]}" and "{cards[user_choice_list[1]]}".')
    time.sleep(2)
    return user_won


def lose_monk(character: dict) -> None:
    """
    Decrease character's Current HP by 2.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: character must contain X- and Y-coordinates, current status, and name
    :postcondition: decreases character's Current HP by 2.

    >>> user_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4, 'KEP': 8, 'Name': 'Chris', 'Level': 'level 3'}
    >>> lose_monk(user_character)
    >>> user_character
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 2, 'KEP': 8, 'Name': 'Chris', 'Level': 'level 3'}
    >>> user_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 2, 'KEP': 7, 'Name': 'Chris', 'Level': 'level 3'}
    >>> lose_monk(user_character)
    >>> user_character
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 0, 'KEP': 7, 'Name': 'Chris', 'Level': 'level 3'}

    """
    character['Current HP'] -= 2


def is_alive(character: dict) -> bool:
    """
    Check if character's Current HP reaches zero or not.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :precondition: user_character must contain X- and Y-coordinates, current status, and name
    :postcondition: checks if the current HP in character reaches zero or not
    :return: a Boolean

    >>> user_character = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 3, 'KEP': 5, 'Level': 'level 2', 'Name': 'Chris'}
    >>> is_alive(user_character)
    True
    >>> user_character = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 0, 'KEP': 3, 'Level': 'level 2', 'Name': 'Chris'}
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
        check_level(character, level_dictionary)
        direction = get_user_choice()
        valid_move = validate_direction(board, character, direction)
        if valid_move:
            move_user(character, direction)

            if is_food_station(character, board):
                eat_food(character, level_dictionary)

            kinkakuji = is_kinkakuji(character, board)
            level_3 = is_achieved_level_3(character)
            if kinkakuji and level_3:
                print_monk_pic()
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
    # game()
    fight_with_monk()


if __name__ == '__main__':
    main()
