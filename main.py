import time


def make_a_board():
    """

    :return:
    """
    board_dict = {}
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

    """
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


def validate_direction():
    """

    :return:
    """
    pass


def move_user():
    """

    :return:
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


def is_food_station():
    """

    :return:
    """
    pass


def eat_food():
    """

    :return:
    """
    pass


def fight_with_monk():
    """

    :return:
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
    while


def main():
    game()


if __name__ == '__main__':
    main()
