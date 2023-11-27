import time
import random
import json


def make_a_board():
    """
    Create a 10 x 10 game board.

    Each point on the game board is represented by coordinates ranging from (0, 0) to (9, 9),
    and each point is assigned a name.
    Special locations on the board have specific coordinates, while others are named "Random Street."
    :postcondition: creates a 10 x 10 game board
    :return: a dictionary where keys are coordinates and values are names of the places
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
    Create a dictionary with character's information.

    This function allows a user to enter character's name.
    After the character's name is determined, this function returns a dictionary with character's information.
    :postcondition: creates a dictionary with character's information
    :return: a dictionary where keys are X- Y-coordinates, Current HP, KEP, and name of the character
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


def show_status_and_map(user_character, board):
    """
    Print user's current location in map and character.

    :param user_character: a dictionary where keys are X- Y-coordinates, Current HP, KEP, and name of the character
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: user_character must conform to the format specified in the parameter
    :postcondition: board must be a dictionary with keys and values described in param board
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
    Ask a user to enter the direction they wish to travel and return the user's choice.

    This function prompts the user to input an integer between 1 and 4 (inclusive).
    If the user enters something other than an integer, the function requests input again.
    :postcondition: the function let a user enter a number until they enter a correct number
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
    Validate if the character can move to the specified direction.

    :param board: a dictionary where keys are coordinates and values are names of the places
    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param direction: an integer of direction users have chosen
    :precondition: board must be a dictionary that contains rows * columns keys and a short description
    :precondition: character must be a dictionary that contains coordinate, current status, and name
    :precondition: direction must be an integer between 1 and 4 inclusive
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
    Update character's X- and Y-coordinates depending on the direction selected by the user.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param direction: an integer between 1 and 4 inclusive
    :precondition: character must be a dictionary that contains coordinate, current status, and name
    :precondition: direction must be an integer between 1 and 4 inclusive
    :postcondition: updates character's X- and Y-coordinates depending on the direction selected by the user
    """
    pass


def is_kinkakuji(character, board):
    """
    Check if the character has reached the goal.

    :param character: a dictionary that contains X- and Y-coordinates, current status, and name
    :param board: a dictionary where keys are coordinates and values are names of the places
    :precondition: character must conform to the format specified in the parameter
    :precondition: board must conform to the format specified in the parameter
    :postcondition: checks if the character is in the goal
    :return: a boolean
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
    :return: a boolean
    """
    encounter_quiz = random.randint(1, 10)
    return encounter_quiz <= 3


def play_quiz(user_character):
    """

    :param user_character:
    :return:
    """
    filename = "quiz.json"
    with open(filename) as file_object:
        quiz_list = json.load(file_object)

    random_number = random.randint(0, 1) # change it later
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
        user_character["KEP"] += 1
    else:
        print("You are wrong, your HP was decreased by 1")
        user_character["Current HP"] -= 1
    print(user_character)


def check_level_up(character):
    """

    :param character:
    :precondition:
    :postcondition:
    """
    current_kep = character['KEP']
    if current_kep <= 3:
        print('Now you are level 1.')
    elif current_kep < 7:
        print('Now you are level 2.')
    else:
        print('You are level 3 now! You\'re ready to fight with monk at Kinkakuji Temple.')


def is_achieved_level_3(character):
    """
    Check if the character reach level 3

    :param character:
    :precondition:
    :postcondition:
    :return: a boolean
    """
    current_level = character['KEP'] >= 7
    return current_level


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
    while True:
        # fight_dictionary = {1: 'rock', 2: 'paper', 3: 'scissors'}
        monk_choice = random.randint(1, 3)
        user_choice = int(input('Monk wants to fight with you. Which do you want to choose? '
                                'Type 1 for rock, 2 for paper, 3 for scissors'))
        if monk_choice == user_choice:
            continue
        elif monk_choice < user_choice:
            if monk_choice == 1 and user_choice == 3:
                return False
            else:
                return True
        else:
            if monk_choice == 3 and user_choice == 1:
                return True
            else:
                return False


def lose_monk(character):
    """

    :param character:
    :precondition:
    :postcondition:
    """
    character['Current HP'] -= 2


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
    make_a_board()
    show_status_and_map()
    game()



if __name__ == '__main__':
    main()
