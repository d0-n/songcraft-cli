"""
CRUD Operations for SongCraft CLI.
Allows users to Create, Read, Update, and Delete data in the database.
"""


from app.user import award_xp

def crud_menu(conn, user):
    """Main CRUD menu loop."""
    while True:
        print("\n  ============================")
        print("  |   MY LIBRARY & DATA      |")
        print("  ============================")
        print("  1. Manage Genres")
        print("  2. Manage Topics")
        print("  3. Manage Tips")
        print("  4. My Song Drafts")
        print("  5. Back to Main Menu")
        print()

        choice = input("  Pick an option (1-5): ").strip()

        if choice == "1":
            manage_genres(conn)
        elif choice == "2":
            manage_topics(conn)
        elif choice == "3":
            manage_tips(conn)
        elif choice == "4":
            manage_songs(conn, user)
        elif choice == "5":
            break
        else:
            print("\n  Invalid choice. Please enter 1-5.")


# ===========================
#  GENRES CRUD
# ===========================

def manage_genres(conn):
    """CRUD sub-menu for genres."""
    while True:
        print("\n  --- Genres ---")
        print("  1. View all genres")
        print("  2. Add a genre")
        print("  3. Update a genre")
        print("  4. Delete a genre")
        print("  5. Back")
        print()

        choice = input("  Pick an option (1-5): ").strip()

        if choice == "1":
            view_all(conn, "genres", ["id", "name", "description"])
        elif choice == "2":
            add_genre(conn)
        elif choice == "3":
            update_genre(conn)
        elif choice == "4":
            delete_genre(conn)
        elif choice == "5":
            break


def add_genre(conn):
    """CREATE: Add a new genre."""
    name = input("\n  Genre name: ").strip()
    if not name:
        print("  Name cannot be empty.")
        return

    description = input("  Description: ").strip()

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO genres (name, description) VALUES (%s, %s)",
        (name, description)
    )
    conn.commit()
    print(f"\n  Added genre '{name}' successfully!")


def update_genre(conn):
    """UPDATE: Edit an existing genre."""
    view_all(conn, "genres", ["id", "name", "description"])

    genre_id = input("\n  Enter the ID of the genre to update: ").strip()
    if not genre_id.isdigit():
        print("  Please enter a valid number.")
        return

    new_name = input("  New name (press Enter to keep current): ").strip()
    new_desc = input("  New description (press Enter to keep current): ").strip()

    cursor = conn.cursor()
    if new_name and new_desc:
        cursor.execute("UPDATE genres SET name = %s, description = %s WHERE id = %s",
                       (new_name, new_desc, int(genre_id)))
    elif new_name:
        cursor.execute("UPDATE genres SET name = %s WHERE id = %s",
                       (new_name, int(genre_id)))
    elif new_desc:
        cursor.execute("UPDATE genres SET description = %s WHERE id = %s",
                       (new_desc, int(genre_id)))
    else:
        print("  Nothing to update.")
        return

    conn.commit()
    print("  Genre updated successfully!")


def delete_genre(conn):
    """DELETE: Remove a genre."""
    view_all(conn, "genres", ["id", "name", "description"])

    genre_id = input("\n  Enter the ID of the genre to delete: ").strip()
    if not genre_id.isdigit():
        print("  Please enter a valid number.")
        return

    confirm = input(f"  Are you sure you want to delete genre {genre_id}? (y/n): ").strip().lower()
    if confirm == "y":
        cursor = conn.cursor()
        cursor.execute("DELETE FROM genres WHERE id = %s", (int(genre_id),))
        conn.commit()
        print("  Genre deleted.")
    else:
        print("  Cancelled.")


# ===========================
#  TOPICS CRUD
# ===========================

def manage_topics(conn):
    """CRUD sub-menu for topics."""
    while True:
        print("\n  --- Topics ---")
        print("  1. View all topics")
        print("  2. Add a topic")
        print("  3. Update a topic")
        print("  4. Delete a topic")
        print("  5. Back")
        print()

        choice = input("  Pick an option (1-5): ").strip()

        if choice == "1":
            view_all(conn, "topics", ["id", "name", "description"])
        elif choice == "2":
            add_topic(conn)
        elif choice == "3":
            update_topic(conn)
        elif choice == "4":
            delete_topic(conn)
        elif choice == "5":
            break


def add_topic(conn):
    """CREATE: Add a new topic."""
    name = input("\n  Topic name: ").strip()
    if not name:
        print("  Name cannot be empty.")
        return

    description = input("  Description: ").strip()

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO topics (name, description) VALUES (%s, %s)",
        (name, description)
    )
    conn.commit()
    print(f"\n  Added topic '{name}' successfully!")


def update_topic(conn):
    """UPDATE: Edit an existing topic."""
    view_all(conn, "topics", ["id", "name", "description"])

    topic_id = input("\n  Enter the ID of the topic to update: ").strip()
    if not topic_id.isdigit():
        print("  Please enter a valid number.")
        return

    new_name = input("  New name (press Enter to keep current): ").strip()
    new_desc = input("  New description (press Enter to keep current): ").strip()

    cursor = conn.cursor()
    if new_name and new_desc:
        cursor.execute("UPDATE topics SET name = %s, description = %s WHERE id = %s",
                       (new_name, new_desc, int(topic_id)))
    elif new_name:
        cursor.execute("UPDATE topics SET name = %s WHERE id = %s",
                       (new_name, int(topic_id)))
    elif new_desc:
        cursor.execute("UPDATE topics SET description = %s WHERE id = %s",
                       (new_desc, int(topic_id)))
    else:
        print("  Nothing to update.")
        return

    conn.commit()
    print("  Topic updated successfully!")


def delete_topic(conn):
    """DELETE: Remove a topic."""
    view_all(conn, "topics", ["id", "name", "description"])

    topic_id = input("\n  Enter the ID of the topic to delete: ").strip()
    if not topic_id.isdigit():
        print("  Please enter a valid number.")
        return

    confirm = input(f"  Are you sure you want to delete topic {topic_id}? (y/n): ").strip().lower()
    if confirm == "y":
        cursor = conn.cursor()
        cursor.execute("DELETE FROM topics WHERE id = %s", (int(topic_id),))
        conn.commit()
        print("  Topic deleted.")
    else:
        print("  Cancelled.")


# ===========================
#  TIPS CRUD
# ===========================

def manage_tips(conn):
    """CRUD sub-menu for tips."""
    while True:
        print("\n  --- Tips ---")
        print("  1. View all tips")
        print("  2. Add a tip")
        print("  3. Update a tip")
        print("  4. Delete a tip")
        print("  5. Back")
        print()

        choice = input("  Pick an option (1-5): ").strip()

        if choice == "1":
            view_tips(conn)
        elif choice == "2":
            add_tip(conn)
        elif choice == "3":
            update_tip(conn)
        elif choice == "4":
            delete_tip(conn)
        elif choice == "5":
            break


def view_tips(conn):
    """READ: Show all tips with their genre."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT tips.id, genres.name, tips.tip_text "
        "FROM tips JOIN genres ON tips.genre_id = genres.id ORDER BY tips.id"
    )
    rows = cursor.fetchall()

    print("\n  ==== ALL TIPS ====")
    for row in rows:
        print(f"  [{row[0]}] ({row[1]}) {row[2]}")
    print()


def add_tip(conn):
    """CREATE: Add a new tip."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM genres ORDER BY id")
    genres = cursor.fetchall()

    print("\n  Available genres:")
    for g in genres:
        print(f"  {g[0]}. {g[1]}")

    genre_id = input("\n  Pick a genre ID for this tip: ").strip()
    if not genre_id.isdigit():
        print("  Please enter a valid number.")
        return

    tip_text = input("  Tip text: ").strip()
    if not tip_text:
        print("  Tip text cannot be empty.")
        return

    cursor.execute(
        "INSERT INTO tips (genre_id, tip_text) VALUES (%s, %s)",
        (int(genre_id), tip_text)
    )
    conn.commit()
    print("  Tip added successfully!")


def update_tip(conn):
    """UPDATE: Edit an existing tip."""
    view_tips(conn)

    tip_id = input("  Enter the ID of the tip to update: ").strip()
    if not tip_id.isdigit():
        print("  Please enter a valid number.")
        return

    new_text = input("  New tip text: ").strip()
    if not new_text:
        print("  Tip text cannot be empty.")
        return

    cursor = conn.cursor()
    cursor.execute("UPDATE tips SET tip_text = %s WHERE id = %s",
                   (new_text, int(tip_id)))
    conn.commit()
    print("  Tip updated successfully!")


def delete_tip(conn):
    """DELETE: Remove a tip."""
    view_tips(conn)

    tip_id = input("  Enter the ID of the tip to delete: ").strip()
    if not tip_id.isdigit():
        print("  Please enter a valid number.")
        return

    confirm = input(f"  Are you sure you want to delete tip {tip_id}? (y/n): ").strip().lower()
    if confirm == "y":
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tips WHERE id = %s", (int(tip_id),))
        conn.commit()
        print("  Tip deleted.")
    else:
        print("  Cancelled.")


# ===========================
#  USER SONGS (DRAFTS) CRUD
# ===========================

def manage_songs(conn, user):
    """CRUD sub-menu for user song drafts."""
    while True:
        print("\n  --- My Song Drafts ---")
        print("  1. View my drafts")
        print("  2. Write a new draft")
        print("  3. Edit a draft")
        print("  4. Delete a draft")
        print("  5. Back")
        print()

        choice = input("  Pick an option (1-5): ").strip()

        if choice == "1":
            view_songs(conn, user)
        elif choice == "2":
            add_song(conn, user)
        elif choice == "3":
            update_song(conn, user)
        elif choice == "4":
            delete_song(conn, user)
        elif choice == "5":
            break


def view_songs(conn, user):
    """READ: List all saved song drafts for the current user."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, genre, created_at FROM user_songs WHERE user_id = %s ORDER BY id", (user['id'],))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("\n  No song drafts saved yet.")
        return

    print("\n  ==== MY SONG DRAFTS ====")
    for row in rows:
        print(f"  [{row[0]}] \"{row[1]}\" ({row[2]}) — {row[3]}")
    print()

    view_id = input("  Enter a draft ID to view full lyrics (or Enter to skip): ").strip()
    if view_id.isdigit():
        cursor.execute("SELECT title, lyrics, genre FROM user_songs WHERE id = %s AND user_id = %s", (int(view_id), user['id']))
        song = cursor.fetchone()
        if song:
            print(f"\n  Title: {song[0]}")
            print(f"  Genre: {song[2]}")
            print("  Lyrics:")
            for line in song[1].split("\n"):
                print(f"    {line}")
            print()
        else:
            print("  Draft not found or you don't have permission.")


def add_song(conn, user):
    """CREATE: Write and save a new song draft."""
    title = input("\n  Song title: ").strip()
    if not title:
        print("  Title cannot be empty.")
        return

    genre = input("  Genre (e.g., Hip-Hop, Pop): ").strip()

    print("  Type your lyrics below. Type 'DONE' on a new line when finished.")
    lyrics_lines = []
    while True:
        line = input("  | ")
        if line.strip().upper() == "DONE":
            break
        lyrics_lines.append(line)

    lyrics = "\n".join(lyrics_lines)
    if not lyrics.strip():
        print("  Lyrics cannot be empty.")
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_songs (user_id, title, lyrics, genre) VALUES (%s, %s, %s, %s)",
        (user['id'], title, lyrics, genre)
    )
    conn.commit()
    print(f"\n  Draft '{title}' saved to secure cloud DB!")
    
    # Gamification
    award_xp(conn, user, 10, "Wrote a song draft")


def update_song(conn, user):
    """UPDATE: Edit a saved song draft."""
    view_songs(conn, user)

    song_id = input("  Enter the ID of the draft to edit: ").strip()
    if not song_id.isdigit():
        print("  Please enter a valid number.")
        return
        
    # Verify ownership
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user_songs WHERE id = %s AND user_id = %s", (int(song_id), user['id']))
    if not cursor.fetchone():
        print("  Draft not found or you don't have permission.")
        return

    new_title = input("  New title (press Enter to keep current): ").strip()

    print("  Type new lyrics (or type 'KEEP' to keep current lyrics):")
    first_line = input("  | ").strip()
    if first_line.upper() == "KEEP":
        new_lyrics = None
    else:
        lyrics_lines = [first_line]
        while True:
            line = input("  | ")
            if line.strip().upper() == "DONE":
                break
            lyrics_lines.append(line)
        new_lyrics = "\n".join(lyrics_lines)

    if new_title and new_lyrics:
        cursor.execute("UPDATE user_songs SET title = %s, lyrics = %s WHERE id = %s",
                       (new_title, new_lyrics, int(song_id)))
    elif new_title:
        cursor.execute("UPDATE user_songs SET title = %s WHERE id = %s",
                       (new_title, int(song_id)))
    elif new_lyrics:
        cursor.execute("UPDATE user_songs SET lyrics = %s WHERE id = %s",
                       (new_lyrics, int(song_id)))
    else:
        print("  Nothing to update.")
        return

    conn.commit()
    print("  Draft updated!")


def delete_song(conn, user):
    """DELETE: Remove a song draft."""
    view_songs(conn, user)

    song_id = input("  Enter the ID of the draft to delete: ").strip()
    if not song_id.isdigit():
        print("  Please enter a valid number.")
        return
        
    # Verify ownership
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user_songs WHERE id = %s AND user_id = %s", (int(song_id), user['id']))
    if not cursor.fetchone():
        print("  Draft not found or you don't have permission.")
        return

    confirm = input(f"  Are you sure you want to delete draft {song_id}? (y/n): ").strip().lower()
    if confirm == "y":
        cursor.execute("DELETE FROM user_songs WHERE id = %s", (int(song_id),))
        conn.commit()
        print("  Draft deleted.")
    else:
        print("  Cancelled.")


# ===========================
#  SHARED HELPER
# ===========================

def view_all(conn, table_name, columns):
    """READ: Display all rows from a given table."""
    cursor = conn.cursor()
    cols = ", ".join(columns)
    cursor.execute(f"SELECT {cols} FROM {table_name} ORDER BY id")
    rows = cursor.fetchall()

    print(f"\n  ==== ALL {table_name.upper()} ====")
    for row in rows:
        print(f"  [{row[0]}] {row[1]}")
        if len(row) > 2 and row[2]:
            print(f"      {row[2]}")
    print()
