import sqlite3
from config import DATABASE_PATH


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        self.connection.execute("PRAGMA foreign_keys = ON")

        self.cursor = self.connection.cursor()

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def fetchone(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def create_tables(self):

        # -----------------------------
        # Colleges
        # -----------------------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS colleges(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            college_name TEXT NOT NULL,

            city TEXT,

            state TEXT,

            email TEXT,

            phone TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # -----------------------------
        # Messes
        # -----------------------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS messes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            college_id INTEGER,

            mess_name TEXT,

            capacity INTEGER,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(college_id)
            REFERENCES colleges(id)
        )
        """)

        # -----------------------------
        # Users
        # -----------------------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            phone TEXT,

            password_hash TEXT NOT NULL,

            role TEXT NOT NULL,

            college_id INTEGER,

            mess_id INTEGER,

            photo TEXT,

            is_active INTEGER DEFAULT 1,

            failed_attempts INTEGER DEFAULT 0,

            last_login TIMESTAMP,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(college_id)
            REFERENCES colleges(id),

            FOREIGN KEY(mess_id)
            REFERENCES messes(id)

        )
        """)

        print("✅ Database Tables Created Successfully")


db = DatabaseManager()
db.create_tables()
