USER_TABLE_NAME = 'users'
GAMES_TABLE_NAME = 'games'


CREATE_GAMES_TABLE = f"""
    CREATE TABLE IF NOT EXISTS {GAMES_TABLE_NAME} (
        id                INTEGER  PRIMARY KEY AUTOINCREMENT,
        user_id           INTEGER  NOT NULL,
        count_of_attempts INTEGER  NOT NULL,
        date_of_the_game  TEXT     NOT NULL,
        FOREIGN KEY (user_id) REFERENCES {USER_TABLE_NAME}(id) ON DELETE CASCADE
    )
    """

CREATE_USERS_TABLE = f"""
    CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME} (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name  TEXT    NOT NULL,
        user_email TEXT    NON NULL,
        password   TEXT    NOT NULL
    )
    """

IS_USER_IN_DB = f"""
    SELECT (count(user_name)>=1) from {USER_TABLE_NAME} where user_name = 
    """

INSERT_USER_QUERY = f"""
    INSERT INTO
    {USER_TABLE_NAME} (user_name, user_email, password)
    values
    """

INSERT_GAME_QUERY = f"""
    INSERT INTO
    {GAMES_TABLE_NAME} (date_of_the_game, user_id, count_of_attempts)
    VALUES
    (datetime('now'), (select id from {USER_TABLE_NAME} where user_name = """
