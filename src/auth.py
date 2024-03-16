"""
Module containing functions for user authentication (login and account creation).
"""

import sqlite3
import hashlib

# SQLite db path
DB_FILE = "../db/key-guardian.db"


def create_users_table():
    """
    Create the user table in the sqlite database
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
		CREATE TABLE IF NOT EXISTS users (
			id INTEGER PRIMARY KEY,
			username TEXT UNIQUE,
			password TEXT
		)
	"""
    )

    conn.commit()
    conn.close()


def hash_password(password):
    """Hash the password using SHA-256 algorithm"""
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    """Registers a new user to KeyGuardian app"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, hashed_password),
        )
        conn.commit()
        print(f"User {username} registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username {username} already exists.")
    finally:
        conn.close()


def login(username, password):
    """Authenticate the user"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (username, hashed_password),
    )
    user_id = cursor.fetchone()

    print(f"DEBUG: Tried to fetch {username} with password {hashed_password}")

    conn.close()

    if user_id:
        print(f"Welcome {username}")
        return True
    else:
        print("Invalid username and password combination.")
        return False
