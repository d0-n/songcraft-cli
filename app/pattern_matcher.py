"""
Pattern Matcher Algorithm.
Finds which legendary artist's writing style matches the user's lyrics.
"""
from app.user import award_xp

def count_syllables(word):
    # simple way to guess syllables by counting vowel groups
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    
    if word[0] in vowels:
        count += 1
        
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            
    if word.endswith("e"):
        count -= 1
        
    if count == 0:
        count = 1
        
    return count

def words_rhyme(word1, word2):
    # checks if last 2 letters are the same
    word1 = word1.lower()
    word2 = word2.lower()
    
    if len(word1) < 2 or len(word2) < 2:
        return word1 == word2
        
    return word1[-2:] == word2[-2:]

def extract_features(lyrics_text):
    # takes a chunk of text and returns 4 important numbers
    lines = [line.strip() for line in lyrics_text.split('\n') if line.strip()]
    
    if not lines:
        return [0, 0, 0, 0]
        
    # 1. average syllables per line
    total_syllables = 0
    for line in lines:
        words = line.split()
        for word in words:
            total_syllables += count_syllables(word)
            
    avg_syllables = total_syllables / len(lines)
    
    # 2. rhyme density
    rhymed_lines = 0
    end_words = []
    
    for line in lines:
        words = line.split()
        if words:
            # remove punctuation from the last word
            clean_word = words[-1].strip(".,!?;:\"'")
            end_words.append(clean_word)
            
    for i in range(len(end_words)):
        has_rhyme = False
        for j in range(len(end_words)):
            if i != j and words_rhyme(end_words[i], end_words[j]):
                has_rhyme = True
                break
        if has_rhyme:
            rhymed_lines += 1
            
    rhyme_density = rhymed_lines / len(lines)
    
    # 3. vocabulary richness (how many different words used)
    all_words = []
    for line in lines:
        for word in line.split():
            clean_word = word.strip(".,!?;:\"'").lower()
            if clean_word:
                all_words.append(clean_word)
                
    if not all_words:
        vocab_richness = 0
    else:
        unique_words = set(all_words)
        vocab_richness = len(unique_words) / len(all_words)
        
    # 4. line length consistency (standard deviation)
    word_counts = []
    for line in lines:
        word_counts.append(len(line.split()))
        
    mean_length = sum(word_counts) / len(word_counts)
    
    squared_diffs = []
    for count in word_counts:
        diff = count - mean_length
        squared_diffs.append(diff * diff)
        
    variance = sum(squared_diffs) / len(squared_diffs)
    line_variance = variance ** 0.5
    
    return [rhyme_density, avg_syllables, vocab_richness, line_variance]

def cosine_similarity(vector_a, vector_b):
    # math formula to see how similar two lists of numbers are
    dot_product = 0.0
    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]
        
    sum_a_squared = 0.0
    for value in vector_a:
        sum_a_squared += value * value
    magnitude_a = sum_a_squared ** 0.5
    
    sum_b_squared = 0.0
    for value in vector_b:
        sum_b_squared += value * value
    magnitude_b = sum_b_squared ** 0.5
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
        
    return dot_product / (magnitude_a * magnitude_b)

def normalize_vector(raw_vector):
    # make all numbers between 0 and 1 so they can be compared fairly
    min_vals = [0.0, 3.0, 0.2, 0.0]
    max_vals = [1.0, 20.0, 0.9, 10.0]
    
    normalized = []
    
    for i in range(4):
        val = raw_vector[i]
        if val < min_vals[i]:
            val = min_vals[i]
        if val > max_vals[i]:
            val = max_vals[i]
            
        scaled = (val - min_vals[i]) / (max_vals[i] - min_vals[i])
        normalized.append(scaled)
        
    return normalized

def find_style_matches(conn, user_vector):
    # compares user vector to every artist in database
    cursor = conn.cursor(dictionary=True) if hasattr(conn.cursor(), 'dictionary') else conn.cursor()
    
    cursor.execute('''
        SELECT name, genre, rhyme_density, avg_syllables, vocab_richness, line_variance, bio, study_tip 
        FROM artist_profiles
    ''')
    
    # support both dictionaries and tuples from mysql
    if hasattr(cursor, 'dictionary'):
        rows = cursor.fetchall()
        artists = rows
    else:
        rows = cursor.fetchall()
        artists = []
        for row in rows:
            artists.append({
                'name': row[0],
                'genre': row[1],
                'rhyme_density': row[2],
                'avg_syllables': row[3],
                'vocab_richness': row[4],
                'line_variance': row[5],
                'bio': row[6],
                'study_tip': row[7]
            })
            
    results = []
    normalized_user = normalize_vector(user_vector)
    
    for artist in artists:
        artist_vector = [
            artist['rhyme_density'],
            artist['avg_syllables'],
            artist['vocab_richness'],
            artist['line_variance']
        ]
        
        normalized_artist = normalize_vector(artist_vector)
        score = cosine_similarity(normalized_user, normalized_artist)
        
        results.append({
            'artist': artist,
            'score': score
        })
        
    # sort by highest score first
    results.sort(key=lambda x: x['score'], reverse=True)
    return results

def draw_bar(value, max_val=1.0, width=20):
    # draws a text progress bar
    filled = int((value / max_val) * width)
    if filled > width:
        filled = width
    empty = width - filled
    return "█" * filled + "░" * empty

def display_results(user_vector, matches, top_n=3):
    print("\n  ┌─────────────────────────────────────────┐")
    print("  │          YOUR WRITING PROFILE           │")
    print("  ├─────────────────────────────────────────┤")
    print(f"  │ Rhyme Density        {user_vector[0]:.2f}  {draw_bar(user_vector[0], 1.0)} │")
    print(f"  │ Syllables/Line      {user_vector[1]:.2f}  {draw_bar(user_vector[1], 20.0)} │")
    print(f"  │ Vocab Richness       {user_vector[2]:.2f}  {draw_bar(user_vector[2], 1.0)} │")
    print(f"  │ Line Variance        {user_vector[3]:.2f}  {draw_bar(user_vector[3], 10.0)} │")
    print("  └─────────────────────────────────────────┘\n")
    
    print("  ┌─────────────────────────────────────────┐")
    print("  │          CLOSEST ARTIST MATCHES         │")
    print("  └─────────────────────────────────────────┘\n")
    
    medals = ["🥇", "🥈", "🥉", "4.", "5."]
    
    for i in range(min(top_n, len(matches))):
        match = matches[i]
        artist = match['artist']
        percentage = int(match['score'] * 100)
        
        print(f"  {medals[i]} {artist['name']} — {percentage}% match")
        print(f"     {artist['bio']}")
        print(f"     -> Study tip: {artist['study_tip']}\n")

def run_pattern_matcher(conn, user):
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║         PATTERN MATCHER ALGORITHM        ║")
    print("  ║  Paste your lyrics below.                ║")
    print("  ║  Type 'DONE' on a new line to finish     ║")
    print("  ╚══════════════════════════════════════════╝\n")
    
    lines = []
    while True:
        line = input("  | ")
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
        
    lyrics_text = "\n".join(lines)
    
    if not lyrics_text.strip():
        print("  Error: No lyrics provided.")
        input("  Press Enter to return to menu... ")
        return
        
    print("\n  Running pattern matching algorithm...")
    
    user_vector = extract_features(lyrics_text)
    
    if sum(user_vector) == 0:
        print("  Error: Not enough text to analyze.")
        input("  Press Enter to return to menu... ")
        return
        
    matches = find_style_matches(conn, user_vector)
    
    display_results(user_vector, matches, top_n=3)
    
    award_xp(conn, user, 20, "Ran Pattern Matcher")
    
    input("  Press Enter to return to menu... ")
