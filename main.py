import random
from db_api import add_user_to_db, check_the_user_in_db
from classes import User

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

    # Авторизация и регистрация.
    register_flag = False
    while not register_flag:
        print("Для доступа к игре, пожалуйста, авторизуйтесь или зарегистрируйтесь!")
        register_flag, user_name = registration_interface()


    # Начало игры авторизованным пользователем.
    print(f"Hello, {user_name}!\nWelcome to my game!\n")
 
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
    flag = False
    user_name = None

    reg_or_auth_flag = input('Вы хотите зарегистрироваться или авторизоваться (R/A)?')
    if reg_or_auth_flag.upper() == 'R':
        flag, user_name = registration()
    elif reg_or_auth_flag.upper() == 'A':
        pass
        # авторизация

    return flag, user_name
 
def registration():
    user_name = None
    try:
        while True:
            user_name = input('Введите Ваше имя ->')
            if check_the_user_in_db(user_name):
                print('Это имя уже занято, попробуйте еще раз!')
                continue
            break

        user_email = input('Введите Ваше электронный адрес ->')
        user_password = input('Придумайте пароль для входа ->')

        new_user = User(user_name, user_email, user_password)
        add_user_to_db(new_user)
        return True, user_name

    except Exception as err:
        print(err)
        print("Что-то пошло не так. Пожалуйста, повторите попытку!")
        return False, user_name

            
        


if __name__ == '__main__':
    game_menu()

