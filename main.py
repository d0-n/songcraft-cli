import os
import sys
from db.connection import get_connection
from db.schema import create_tables
from db.seed import seed_data, is_seeded
from app.menu import main_menu


def initialize_db():
    conn = get_connection()
    create_tables(conn)
    if not is_seeded(conn):
        seed_data(conn)
    return conn


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("  ╔══════════════════════════════════════╗")
    print("  ║          Welcome to SongCraft         ║")
    print("  ║     Your Songwriting Guide Tool       ║")
    print("  ╚══════════════════════════════════════╝")
    print()

    conn = initialize_db()
    try:
        main_menu(conn)
    except KeyboardInterrupt:
        print("\n\n  Exiting SongCraft...")
    finally:
        conn.close()

    print("\n  Thanks for using SongCraft. Happy writing!\n")


if __name__ == "__main__":
    main()
