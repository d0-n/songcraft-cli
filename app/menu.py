from app.guide import run_guide
from app.display import print_header, print_divider


def main_menu(conn):
    while True:
        print("\n  ============================")
        print("  |       MAIN MENU         |")
        print("  ============================")
        print("  1. Start Songwriting Guide")
        print("  2. Browse Genres")
        print("  3. Browse Topics")
        print("  4. Exit")
        print()

        choice = input("  Pick an option (1-4): ").strip()

        if choice == "1":
            run_guide(conn)
        elif choice == "2":
            browse_genres(conn)
        elif choice == "3":
            browse_topics(conn)
        elif choice == "4":
            break
        else:
            print("\n  Invalid choice. Please enter 1, 2, 3, or 4.")


def browse_genres(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM genres ORDER BY id")
    genres = cursor.fetchall()

    print_header("ALL GENRES")
    for genre in genres:
        print(f"  {genre['id']}. {genre['name']}")
        print(f"     {genre['description']}")
        print()

    print_divider()
    input("  Press Enter to go back... ")


def browse_topics(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM topics ORDER BY id")
    topics = cursor.fetchall()

    print_header("SONG TOPICS")
    for topic in topics:
        print(f"  {topic['id']}. {topic['name']}")
        print(f"     {topic['description']}")
        print()

    print_divider()
    input("  Press Enter to go back... ")
