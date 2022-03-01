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


def check_the_user_in_db(user_name : str, check_query = IS_USER_IN_DB, create_table_query = CREATE_USERS_TABLE) -> bool:
    result = False
    try:
        connection = create_connection()
        query = check_query + f"'{user_name}'"
        execute_query(connection, create_table_query)
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


def add_gameround_to_db(user_name : str, attempts_count : int, victory : int, insert_game_query = INSERT_GAME_QUERY, create_games_table = CREATE_GAMES_TABLE):
    try:
        connection = create_connection()
        query = insert_game_query + f"'{user_name}'), {attempts_count}, {victory})"
        execute_query(connection, create_games_table)
        execute_query(connection, query)
        result = True
    except Error as err:
        print(err)
        result = False
    return result


def check_users_creads(user_name : str, user_password : str, check_query = IS_USER_IN_DB) -> bool:
    flag = False
    try:
        connection = create_connection()
        query = check_query + f"'{user_name}' AND password = '{user_password}'"
        cursor = execute_query(connection, query)
        if cursor:
            result = cursor.fetchone()[0]
            if result == 1:
                flag = True

    except Error as err:
        print(err) 

    return flag


if __name__ == "__main__":
    user = User('Alex', 'Alex@mail.ru', '123')
    add_user_to_db(user)
    add_gameround_to_db('Alex', 66, 1)