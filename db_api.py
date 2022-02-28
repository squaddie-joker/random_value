import sqlite3
from sqlite3 import Error

path_to_db = 'game_db.db'

def crate_the_user_table(db_path : str, table_name : str):
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT    NOT NULL,
        password  TEXT    NOT NULL
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
    


def execute_select_query(connection : sqlite3.Connection, query : str):
    result = None

    try:
        cursor = connection.cursor()
        result = cursor.execute(query)

    except Error as err:
        print(err)

    return result

def check_the_existence_of_user_in_table(connection : sqlite3.Connection, user_name : str, table_name : str)-> bool:
    query = f"""
    SELECT (count(user_name)>=1) from {table_name} where user_name = "{user_name}"
    """
    result = execute_select_query(connection, query).fetchone()[0]
    
    if result[0] == 1:
        return True
    else:
        return False

def add_user_to_the_table(table_name : str, user_name : str, password : str, db_path : str):
    crate_the_user_table(db_path, table_name)
    connection = create_connection(db_path)

    query = f"""
    INSERT INTO
    {table_name} (user_name, password)
    values
    ('{user_name}', {password})
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



if __name__ == "__main__":
    connection = create_connection(path_to_db)
    res = check_the_existence_of_user_in_table(connection, 'Alex', "users")
    print(res)