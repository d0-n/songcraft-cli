import math


def login_user(conn):
    """
    Simple login system for SongCraft CLI.
    Asks for a username. If it exists, logs them in.
    If it doesn't exist, creates a new profile.
    
    Returns:
        dict: User data containing id, username, xp, level
    """
    print("\n  ============================")
    print("  |   SONGCRAFT USER LOGIN   |")
    print("  ============================")
    
    while True:
        username = input("  Enter your username (or type 'NEW' to create one): ").strip()
        
        if not username:
            continue
            
        cursor = conn.cursor(dictionary=True) if hasattr(conn.cursor(), 'dictionary') else conn.cursor()
        
        if hasattr(cursor, 'dictionary'):
            cursor.execute("SELECT id, username, xp, level FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
        else:
            # Fallback to tuple unpacking
            cursor.execute("SELECT id, username, xp, level FROM users WHERE username = %s", (username,))
            row = cursor.fetchone()
            if row:
                user = {"id": row[0], "username": row[1], "xp": row[2], "level": row[3]}
            else:
                user = None
            
        if user:
            print(f"\n  Welcome back, {user['username']}! (Level {user['level']} | {user['xp']} XP)")
            return user
            
        # If user doesn't exist or typed 'NEW'
        if username.upper() == 'NEW':
            username = input("  Choose a new username: ").strip()
            if not username:
                print("  Username cannot be empty.")
                continue
                
            # Check if name is taken
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                print("  That username is already taken. Try another.")
                continue
                
        # Create new user
        print(f"\n  Creating profile for '{username}'...")
        cursor.execute("INSERT INTO users (username, xp, level) VALUES (%s, %s, %s)", (username, 0, 1))
        conn.commit()
        
        # Fetch the newly created user
        new_id = cursor.lastrowid
        user = {"id": new_id, "username": username, "xp": 0, "level": 1}
        
        print("  Profile created successfully!")
        print(f"  Welcome, {user['username']}! You are starting at Level 1.")
        return user


def calculate_level(xp):
    """
    Calculate the user's level based on their total XP.
    Formula: Level = Floor(1 + sqrt(XP / 50))
    
    - 0 XP -> Level 1
    - 150 XP -> Level 2
    - 400 XP -> Level 3
    - 750 XP -> Level 4
    """
    return math.floor(1 + math.sqrt(xp / 50))


def award_xp(conn, user, amount, reason=""):
    """
    Award XP to a user and check for level ups.
    Updates the database and the active user dictionary.
    """
    old_level = user['level']
    new_xp = user['xp'] + amount
    new_level = calculate_level(new_xp)
    
    # Update dictionary
    user['xp'] = new_xp
    user['level'] = new_level
    
    # Update database
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET xp = %s, level = %s WHERE id = %s", (new_xp, new_level, user['id']))
    conn.commit()
    
    if reason:
        print(f"\n  ⭐ +{amount} XP ({reason})")
    else:
        print(f"\n  ⭐ +{amount} XP awarded!")
        
    # Check for level up
    if new_level > old_level:
        print()
        print("  ╔══════════════════════════════════════╗")
        print("  ║            LEVEL UP! 🎉             ║")
        print(f"  ║   Congratulations, {user['username']}!     ║")
        print(f"  ║      You are now LEVEL {new_level:2}          ║")
        print("  ╚══════════════════════════════════════╝")
        print()
