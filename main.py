import os
import sys

# Fix Unicode output on Windows (box-drawing chars, emojis)
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from db.connection import get_connection
from db.schema import create_tables
from db.seed import seed_data, is_seeded
from app.menu import main_menu
from app.user import login_user


def initialize_db():
    """Connect to MySQL, create tables, and seed data if needed."""
    conn = get_connection()
    if conn is None:
        print("\n  Could not connect to the database. Exiting.")
        sys.exit(1)

    create_tables(conn)
    if not is_seeded(conn):
        print("  First-time setup: populating database...")
        seed_data(conn)
        print("  Done!")

    return conn


def main():
    """Entry point for SongCraft CLI."""
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("  ╔══════════════════════════════════════╗")
    print("  ║          Welcome to SongCraft         ║")
    print("  ║     Your Songwriting Guide Tool       ║")
    print("  ╚══════════════════════════════════════╝")
    print()

    conn = initialize_db()
    try:
        current_user = login_user(conn)
        main_menu(conn, current_user)
    except KeyboardInterrupt:
        print("\n\n  Exiting SongCraft...")
    finally:
        conn.close()

    print("\n  Thanks for using SongCraft. Happy writing!\n")


if __name__ == "__main__":
    main()
