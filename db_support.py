import datetime
import sqlite3


def init_db(db_name) -> None:
    '''
    Создаём структуру базы.
    '''
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS messages(
            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME,
            sender TEXT,
            text TEXT
        );
        '''
    )
    conn.commit()
    conn.close()


def load_messages(db_name: str):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
        '''
        SELECT sender, date, text
        FROM messages
        ORDER BY date;
        '''
    )
    sql_data = cur.fetchall()
    conn.close()
    messages = []
    for row in sql_data:
        message = {}
        message['sender'], message['time'], message['text'] = row
        messages.append(message)
    return messages


def add_message(db_name, text, sender,):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    messages = [[datetime.datetime.now(), sender, text]]

    cur.executemany(
        '''INSERT INTO messages (date, sender, text) VALUES(?, ?, ?);''',
        messages
    )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    print('This is modul db_support to messager_with_sqlite')
