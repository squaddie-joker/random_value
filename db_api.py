import sqlite3

path_to_db = 'game_db'

def crate_the_user_table():
    query = """
    CREATE IF NOT EXIST users (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT    NOT NULL
    )
    """

def crate_the_games_table():
    query = """
    CREATE IF NOT EXIST games (
        id                INTEGER  PRIMARY KEY AUTOINCREMENT,
        user_id           INTEGER  NOT NULL,
        count_of_attempts INTEGER, NOT NULL,
        random_value      INTEGER, NOT NULL,
        date_of_the_game  TEXT
    )
    """
