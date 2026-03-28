from app.guide import run_guide
from app.pattern_matcher import run_pattern_matcher
from app.crud import crud_menu


def main_menu(conn, user):
    """Main menu loop for SongCraft CLI."""
    while True:
        print("\n  ============================")
        print("  |       MAIN MENU         |")
        print(f"  | User: {user['username']:<12} |")
        print(f"  | Level: {user['level']} (XP: {user['xp']:<4}) |")
        print("  ============================")
        print("  1. Start Songwriting Guide")
        print("  2. Browse Genres")
        print("  3. Browse Topics")
        print("  4. Pattern Matcher")
        print("  5. My Library & Data")
        print("  6. Exit")
        print()

        choice = input("  Pick an option (1-6): ").strip()

        if choice == "1":
            run_guide(conn)
        elif choice == "2":
            browse_genres(conn)
        elif choice == "3":
            browse_topics(conn)
        elif choice == "4":
            run_pattern_matcher(conn, user)
        elif choice == "5":
            crud_menu(conn, user)
        elif choice == "6":
            break
        else:
            print("\n  Invalid choice. Please enter 1-6.")


def browse_genres(conn):
    """Display all genres."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM genres ORDER BY id")
    genres = cursor.fetchall()

    print("\n  ==========================")
    print("  |      ALL GENRES        |")
    print("  ==========================")
    print()
    for genre in genres:
        print(f"  {genre[0]}. {genre[1]}")
        print(f"     {genre[2]}")
        print()

    print("  " + "-" * 40)
    input("  Press Enter to go back... ")


def browse_topics(conn):
    """Display all topics."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM topics ORDER BY id")
    topics = cursor.fetchall()

    print("\n  ==========================")
    print("  |     SONG TOPICS        |")
    print("  ==========================")
    print()
    for topic in topics:
        print(f"  {topic[0]}. {topic[1]}")
        print(f"     {topic[2]}")
        print()

    print("  " + "-" * 40)
    input("  Press Enter to go back... ")
