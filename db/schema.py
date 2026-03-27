def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS structures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_id INTEGER NOT NULL,
            section_name TEXT NOT NULL,
            section_order INTEGER NOT NULL,
            bar_count TEXT,
            description TEXT,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rhyme_schemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_id INTEGER NOT NULL,
            pattern TEXT NOT NULL,
            name TEXT,
            example TEXT,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_id INTEGER NOT NULL,
            tip_text TEXT NOT NULL,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    conn.commit()
