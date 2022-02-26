import random

def compare_values(random_value : int, user_value : int):
    int_user_value = int(user_value)
    if random_value == int_user_value:
        print(f'Congratulations on your victory! {str(int_user_value)} is really the number I intended')
        return True
    elif random_value < int_user_value:
        print(f'No, my value is less that your one. Pleas, try again.')
        return False
    else:
        print(f'No, my value is more that your one. Pleas, try again.')
        return False


def check_the_value(value):
    try:
        int_value = int(value)
    except:
        int_value = None

    return int_value


def pritn_hello_massege(name='user'):
    hello_string = f"Hello, {name}! Now lets to play.\nI've made a number, so, try to guess it!"
    print(hello_string)
    

def game_round(name):
    pritn_hello_massege(name)

    total_count = 10
    count = 1
    random_number = random.randint(0, 1000)

    while count <= total_count:
        user_value = input(f'Enter you value ({count}/{total_count} attempt) ->')

        if check_the_value(user_value) == 'None':
            print('The input value must be an integer! Try again!')
            continue

        if compare_values(random_number, user_value):
            break
        else:
            count+=1


if __name__ == '__main__':
    game_round('User1')


