import sqlite3


class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            telegram_id INTEGER NOT NULL,
            registration_date TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_user(self, telegram_id, registration_date):
        query = """
        INSERT INTO users (telegram_id, registration_date)
        VALUES (?, ?)
        """
        self.conn.execute(query, (telegram_id, registration_date))
        self.conn.commit()

    def get_user(self, telegram_id):
        query = """
        SELECT * FROM users WHERE telegram_id = ?
        """
        cursor = self.conn.execute(query, (telegram_id,))
        return cursor.fetchone()


    def database_konkurs(konkurs):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO konkurs (new_konkurs) VALUES (?)""", (konkurs,))
        conn.commit()
        conn.close()
        return True



