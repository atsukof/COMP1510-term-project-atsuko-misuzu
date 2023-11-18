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

    :return:
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

def show_status_and_map():
    """

    :return:
    """
    pass


def get_user_choice():
    """

    :return:
    """
    pass


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


def game():
    """
    Run the game
    """
    board = make_a_board()
    character = make_character()
    instruction()


def main():
    game()


if __name__ == '__main__':
    main()
