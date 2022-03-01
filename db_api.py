from multiprocessing import connection
import sqlite3
from sqlite3 import Error
from sqlite_queries import *
from classes import User

PATH_TO_DB = 'game_db.db'


def create_connection() -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(PATH_TO_DB)
    except Error as err:
        print(err)
    return connection


def execute_query(connection : sqlite3.Connection, query : str):
    
    try:
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
    except Error as err:
        print(err)
        result = False
    return result


def check_the_user_in_db(user_name : str, check_query = IS_USER_IN_DB) -> bool:
    result = False
    try:
        connection = create_connection()
        query = check_query + f"'{user_name}'"
        cursor = execute_query(connection, query)
        if cursor:
            result = cursor.fetchone()[0]
    except Error as err:
        print(err) 
    return result


def add_user_to_db(user : User, insert_user_query = INSERT_USER_QUERY, create_table_query = CREATE_USERS_TABLE):
    try:
        connection = create_connection()
        query = insert_user_query + f"\n('{user.user_name}','{user.user_email}','{user.user_password}')"
        execute_query(connection, create_table_query)
        flag = check_the_user_in_db(user.user_name)
        if flag == 0:
            execute_query(connection, query)
        elif flag == 1:
            print(f"Пользоваель с именем '{user.user_name}' уже существует. Выберите другое имя!")
        result = True
    except Error as err:
        print(err)
        result = False
    return result


def add_gameround_to_db(user_name : str, attempts_count : int, insert_game_query = INSERT_GAME_QUERY, create_games_table = CREATE_GAMES_TABLE):
    try:
        connection = create_connection()
        query = insert_game_query + f"'{user_name}'), {attempts_count})"
        execute_query(connection, create_games_table)
        execute_query(connection, query)
        result = True
    except Error as err:
        print(err)
        result = False
    return result



if __name__ == "__main__":
    new_user = User('Alex', 'laa451@mail.ru', 'qwerty123')
    add_gameround_to_db(new_user.user_name, 10)