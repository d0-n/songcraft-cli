import os
from app.display import (
    show_structure, show_rhyme_schemes, show_tips,
    show_genre_info, show_topic_info, print_header, print_divider
)


def run_guide(conn):
    cursor = conn.cursor()

    # step 1: pick a topic
    print_header("STEP 1: WHAT ARE YOU WRITING ABOUT?")
    cursor.execute("SELECT id, name, description FROM topics ORDER BY id")
    topics = cursor.fetchall()

    for topic in topics:
        print(f"  {topic['id']}. {topic['name']}")
    print(f"  {len(topics) + 1}. Custom topic (type your own)")
    print()

    selected_topic = None
    while True:
        pick = input("  Choose a topic number: ").strip()
        if pick.isdigit():
            pick = int(pick)
            if 1 <= pick <= len(topics):
                selected_topic = topics[pick - 1]
                break
            elif pick == len(topics) + 1:
                custom = input("  Type your topic: ").strip()
                if custom:
                    selected_topic = {"name": custom, "description": "Custom topic chosen by you."}
                    break
                else:
                    print("  Topic can't be empty. Try again.")
            else:
                print("  Invalid number. Try again.")
        else:
            print("  Please enter a number.")

    show_topic_info(selected_topic)

    # step 2: pick a genre
    print_header("STEP 2: PICK YOUR GENRE")
    cursor.execute("SELECT id, name, description FROM genres ORDER BY id")
    genres = cursor.fetchall()

    for genre in genres:
        print(f"  {genre['id']}. {genre['name']}")
    print()

    selected_genre = None
    while True:
        pick = input("  Choose a genre number: ").strip()
        if pick.isdigit():
            pick = int(pick)
            if 1 <= pick <= len(genres):
                selected_genre = genres[pick - 1]
                break
            else:
                print("  Invalid number. Try again.")
        else:
            print("  Please enter a number.")

    show_genre_info(selected_genre)
    genre_id = selected_genre["id"]

    # step 3: show song structure
    cursor.execute(
        "SELECT section_name, section_order, bar_count, description "
        "FROM structures WHERE genre_id = ? ORDER BY section_order",
        (genre_id,)
    )
    sections = cursor.fetchall()
    show_structure(sections)
    input("  Press Enter to continue... ")

    # step 4: show rhyme schemes
    cursor.execute(
        "SELECT pattern, name, example FROM rhyme_schemes WHERE genre_id = ?",
        (genre_id,)
    )
    schemes = cursor.fetchall()
    show_rhyme_schemes(schemes)
    input("  Press Enter to continue... ")

    # step 5: show tips
    cursor.execute(
        "SELECT tip_text FROM tips WHERE genre_id = ?",
        (genre_id,)
    )
    tips = cursor.fetchall()
    show_tips(tips)

    # step 6: option to save summary
    print()
    save = input("  Would you like to save a summary to a file? (y/n): ").strip().lower()
    if save == "y":
        save_summary(selected_topic, selected_genre, sections, schemes, tips)
    else:
        print("\n  No worries! Good luck with your song.")

    input("\n  Press Enter to return to the main menu... ")


def save_summary(topic, genre, sections, schemes, tips):
    filename = f"songcraft_{genre['name'].lower().replace(' ', '_')}_guide.txt"

    with open(filename, "w") as f:
        f.write("SongCraft - Songwriting Guide Summary\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Topic: {topic['name']}\n")
        f.write(f"Genre: {genre['name']}\n\n")

        f.write("SONG STRUCTURE\n")
        f.write("-" * 30 + "\n")
        for section in sections:
            f.write(f"  {section['section_order']}. {section['section_name']} "
                    f"({section['bar_count']} bars)\n")
            f.write(f"     {section['description']}\n")
        f.write("\n")

        f.write("RHYME SCHEMES\n")
        f.write("-" * 30 + "\n")
        for scheme in schemes:
            f.write(f"  {scheme['name']} ({scheme['pattern']})\n")
            f.write(f"  Example: {scheme['example']}\n\n")

        f.write("TIPS\n")
        f.write("-" * 30 + "\n")
        for i, tip in enumerate(tips):
            f.write(f"  {i + 1}. {tip['tip_text']}\n")

    print(f"\n  Summary saved to: {filename}")
