import sqlite3
from sqlite3 import Error

path_to_db = 'game_db.db'

def crate_the_user_table(db_path : str, table_name : str):
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT    NOT NULL
    )
    """
    connection = create_connection(db_path)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
        except Error as err:
            print(err)
    connection.close()

def crate_the_games_table(db_path : str):
    query = f"""
    CREATE TABLE IF NOT EXISTS games (
        id                INTEGER  PRIMARY KEY AUTOINCREMENT,
        user_id           INTEGER  NOT NULL,
        count_of_attempts INTEGER, NOT NULL,
        random_value      INTEGER, NOT NULL,
        date_of_the_game  TEXT
    )
    """
    

def add_user_to_the_table(table_name : str, user_name : str, db_path : str):
    crate_the_user_table(db_path, table_name)
    connection = create_connection(db_path)

    query = f"""
    INSERT INTO
    {table_name} (user_name)
    values
    ('{user_name}')
    """

    if connection:
        try:
            cursor = connection.cursor()
            status_code = cursor.execute(query)
            connection.commit()
        except Error as err:
            print(err)
            status_code = False

    return status_code
        

def create_connection(db_path : str) -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(db_path)
    except Error as err:
        print(err)

    return connection
