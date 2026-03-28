import mysql.connector

# --- Aiven MySQL connection credentials ---
try:
    from db.config import DB_PASSWORD
except ImportError:
    # Default placeholder if config is missing
    DB_PASSWORD = "ENTER_YOUR_PASSWORD_HERE"

DB_HOST = "mysql-1a1648ef-alustudent-000.i.aivencloud.com"
DB_PORT = 17271
DB_USER = "avnadmin"
DB_NAME = "songcraft"


def get_connection():
    """Connect to the Aiven MySQL database and return the connection."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database="songcraft",
            ssl_disabled=False
        )
        return conn
    except mysql.connector.Error as e:
        print(f"\n  [!] Database connection failed: {e}")
        print("  [!] Make sure you have internet access and credentials are correct.")
        return None


def close_connection(conn):
    """Safely close the database connection."""
    if conn:
        conn.close()