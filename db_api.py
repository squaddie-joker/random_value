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
    result = True
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(err)
        result = False
    return result


def add_user_to_db(user : User, insert_user_query = INSERT_USER_QUERY, create_table_query = CREATE_USERS_TABLE):
    try:
        connection = create_connection()
        query = insert_user_query + f"\n('{user.user_name}','{user.user_email}','{user.user_password}')"
        execute_query(connection, create_table_query)
        execute_query(connection, query)
        result = True
    except Error as err:
        print(err)
        result = False
    return result


def check_the_user_in_db(user_name : str, check_query = IS_USER_IN_DB) -> bool:
    try:
        connection = create_connection()
        query = check_query + f"'{user_name}'"
        cursor = execute_query(connection, query)
        result = cursor.fetchone()[0]
    except Error as err:
        print(err)
        result = False
    return result


if __name__ == "__main__":
    new_user = User('Alex', 'laa451@mail.ru', 'qwerty123')
    add_user_to_db(new_user)