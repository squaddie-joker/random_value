import random
from db_api import add_user_to_the_table

path_to_db = 'game_db.db'

def compare_values(random_value : int, user_value : int) -> int:
    result = random_value - int(user_value)
    return result
    

def check_the_value(value):
    try:
        int_value = int(value)
    except:
        int_value = None

    return int_value


def pritn_hello_massege(name='user'):
    hello_string = f"\nOk, {name}! Now lets to play.\nI've made a number, so, try to guess it!\n"
    print(hello_string)


def print_win_message(user_value : int, count : int):
    win_string = f"You win! My hidden number is {str(user_value)}! You did it on the {count} try!"
    print(win_string)


def game_round(name):
    pritn_hello_massege(name)

    total_count = 12
    count = 1
    random_number = random.randint(0, 1000)

    while count <= total_count:
        user_value = input(f'Enter you value ({count}/{total_count} attempt) ->')

        if check_the_value(user_value) == 'None':
            print('The input value must be an integer! Try again!')
            continue

        check_flag = compare_values(random_number, user_value)
        if check_flag == 0:
            print_win_message(user_value, count)
            break
        elif check_flag > 0:
            print(f"No, my value is more than {user_value}")
        else:
            print(f"No, my value is less than {user_value}")

        count+=1
        if count <= total_count:
            print("Try again!")
        if count == total_count:
            print("It's your last attempt!")
        if count > total_count:
            print("You have exhausted all your attempts!")
            break


def game_menu():
    print("Hello!\nWelcome to my game!\n")
    user_name = input("So, what is your name?\n_")
    add_user_to_the_table('users', user_name, path_to_db)
    print(f"Nice to meet you, {user_name}!")
    while True:
        answe = input("Do you want to play with me? (Y/n)")
        if answe.upper() == 'Y':
            game_round(user_name)
        elif answe.lower() == 'n':
            print(f'Good bay, {user_name}!')
            break
        else:
            print("Sorry, I don't andarsand you. Please, try again!")


def registration_interface():
    user_name = input("Enter you user_name: ")
    #user_name_flag = check_the_existence_of_the_user(user_name)

if __name__ == '__main__':
    game_menu()

