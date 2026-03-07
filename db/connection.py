import sqlite3
import os

DB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(DB_DIR, "songcraft.db")


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def close_connection(conn):
    if conn:
        conn.close()
