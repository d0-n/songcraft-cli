def create_tables(conn):
    """Create all database tables if they don't already exist."""
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS structures (
            id INT AUTO_INCREMENT PRIMARY KEY,
            genre_id INT NOT NULL,
            section_name VARCHAR(100) NOT NULL,
            section_order INT NOT NULL,
            bar_count VARCHAR(20),
            description TEXT,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rhyme_schemes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            genre_id INT NOT NULL,
            pattern VARCHAR(50) NOT NULL,
            name VARCHAR(100),
            example TEXT,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tips (
            id INT AUTO_INCREMENT PRIMARY KEY,
            genre_id INT NOT NULL,
            tip_text TEXT NOT NULL,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS artist_profiles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            genre VARCHAR(100) NOT NULL,
            rhyme_density FLOAT NOT NULL,
            avg_syllables FLOAT NOT NULL,
            vocab_richness FLOAT NOT NULL,
            line_variance FLOAT NOT NULL,
            bio TEXT,
            study_tip TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            xp INT DEFAULT 0,
            level INT DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_songs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            title VARCHAR(200) NOT NULL,
            lyrics TEXT NOT NULL,
            genre VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
