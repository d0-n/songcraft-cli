def is_seeded(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM genres")
    count = cursor.fetchone()[0]
    return count > 0


def seed_data(conn):
    cursor = conn.cursor()

    # --- genres ---
    genres = [
        ("Pop", "Mainstream genre known for catchy melodies, hooks, and accessible lyrics. "
                "Pop songs often follow a tight verse-chorus structure and aim for wide appeal."),
        ("Rock", "Guitar-driven genre with strong rhythms and powerful vocals. "
                 "Rock spans from classic to modern styles with room for solos and raw energy."),
        ("Hip-Hop", "Rhythm and poetry based genre centered on lyrical flow, beats, and storytelling. "
                    "Verses are typically 16 bars with a catchy hook."),
        ("R&B", "Soulful genre blending rhythm, blues, and modern production. "
                "R&B focuses on smooth melodies, emotional vocals, and themes of love."),
        ("Country", "Storytelling genre rooted in folk traditions. Country songs are heartfelt, "
                    "often narrative-driven with themes of life, love, and the land."),
        ("Afrobeat", "Rhythmic genre originating from West Africa, combining African musical styles "
                     "with funk and jazz elements. Known for grooves, call-and-response, and dance energy.")
    ]
    cursor.executemany("INSERT INTO genres (name, description) VALUES (?, ?)", genres)

    # --- topics ---
    topics = [
        ("Love", "Songs about romantic love, attraction, and deep connection with another person."),
        ("Heartbreak", "Songs dealing with loss, breakups, and the pain of love gone wrong."),
        ("Celebration", "Upbeat songs about joy, partying, achievements, and good times."),
        ("Struggle", "Songs about overcoming hardship, perseverance, and the grind of daily life."),
        ("Identity", "Songs exploring who you are, self-discovery, and personal growth."),
        ("Social Issues", "Songs addressing inequality, justice, community problems, and activism."),
        ("Freedom", "Songs about liberation, independence, and breaking free from constraints."),
        ("Friendship", "Songs celebrating bonds between friends, loyalty, and togetherness.")
    ]
    cursor.executemany("INSERT INTO topics (name, description) VALUES (?, ?)", topics)

    # --- structures ---
    # get genre ids
    cursor.execute("SELECT id, name FROM genres")
    genre_map = {}
    for row in cursor.fetchall():
        genre_map[row[1]] = row[0]

    structures = []

    # Pop structure
    pop_id = genre_map["Pop"]
    pop_sections = [
        (1, "Intro", "4", "Sets the mood with a musical hook or soft instrumental opening"),
        (2, "Verse 1", "8", "Introduces the story or theme with fresh lyrics each time"),
        (3, "Pre-Chorus", "4", "Builds tension and anticipation leading into the chorus"),
        (4, "Chorus", "8", "The main hook with the catchiest melody and repeating lyrics"),
        (5, "Verse 2", "8", "Continues the story with new lyrics over the same melody"),
        (6, "Pre-Chorus", "4", "Same buildup section leading back to the chorus"),
        (7, "Chorus", "8", "Repeat of the main hook to drive the song home"),
        (8, "Bridge", "8", "A shift in melody or mood that adds variety before the final chorus"),
        (9, "Final Chorus", "8", "Last repetition of the hook often with added energy or harmonies"),
        (10, "Outro", "4", "Wraps up the song, can fade out or end with a final note")
    ]
    for order, name, bars, desc in pop_sections:
        structures.append((pop_id, name, order, bars, desc))

    # Rock structure
    rock_id = genre_map["Rock"]
    rock_sections = [
        (1, "Intro / Riff", "4-8", "Opens with a guitar riff or drum pattern that sets the energy"),
        (2, "Verse 1", "8", "Delivers the opening narrative with a steady rhythm"),
        (3, "Chorus", "8", "The powerful singalong section with the main message"),
        (4, "Verse 2", "8", "Advances the story or adds a new perspective"),
        (5, "Chorus", "8", "Repeat of the chorus building momentum"),
        (6, "Guitar Solo", "8-16", "An instrumental break showcasing skill and emotion"),
        (7, "Bridge", "8", "A contrasting section that shifts the dynamic before the finale"),
        (8, "Chorus", "8", "Final chorus often played with maximum intensity"),
        (9, "Outro", "4-8", "Closing section, sometimes ending abruptly or fading out")
    ]
    for order, name, bars, desc in rock_sections:
        structures.append((rock_id, name, order, bars, desc))

    # Hip-Hop structure
    hiphop_id = genre_map["Hip-Hop"]
    hiphop_sections = [
        (1, "Intro / Beat Drop", "4", "Beat starts playing, may include a vocal tag or ad-lib"),
        (2, "Hook", "8", "The catchy repeating section that anchors the whole track"),
        (3, "Verse 1", "16", "First verse where the artist establishes their flow and story"),
        (4, "Hook", "8", "Return to the hook to keep the listener locked in"),
        (5, "Verse 2", "16", "Second verse with deeper content or a different angle"),
        (6, "Hook", "8", "Another repeat of the hook section"),
        (7, "Bridge / Verse 3", "8-16", "Optional section with a change in flow or new content"),
        (8, "Hook", "8", "Final repeat of the hook to close out the track"),
        (9, "Outro", "4", "Beat fades or the artist signs off with final words")
    ]
    for order, name, bars, desc in hiphop_sections:
        structures.append((hiphop_id, name, order, bars, desc))

    # R&B structure
    rnb_id = genre_map["R&B"]
    rnb_sections = [
        (1, "Intro", "4", "Smooth instrumental or vocal opening that sets the tone"),
        (2, "Verse 1", "8", "Begins the emotional narrative with melodic delivery"),
        (3, "Pre-Chorus", "4", "Builds anticipation with rising melody or harmonies"),
        (4, "Chorus", "8", "The soulful centerpiece with the strongest melodic hook"),
        (5, "Verse 2", "8", "Deepens the story with new details and vocal runs"),
        (6, "Pre-Chorus", "4", "Reconnects the verse to the chorus with emotional buildup"),
        (7, "Chorus", "8", "Returns to the main hook with added vocal embellishments"),
        (8, "Bridge", "8", "A reflective or climactic moment that shifts the mood"),
        (9, "Chorus / Outro", "8", "Final chorus that may blend into a smooth outro")
    ]
    for order, name, bars, desc in rnb_sections:
        structures.append((rnb_id, name, order, bars, desc))

    # Country structure
    country_id = genre_map["Country"]
    country_sections = [
        (1, "Intro", "4", "Simple instrumental opening often with acoustic guitar or fiddle"),
        (2, "Verse 1", "8", "Paints a picture or tells the beginning of the story"),
        (3, "Chorus", "8", "The emotional core with the main message and song title"),
        (4, "Verse 2", "8", "Adds depth to the story with new details or a twist"),
        (5, "Chorus", "8", "Returns to the heart of the song"),
        (6, "Bridge", "4-8", "A reflective moment or change in perspective before the final push"),
        (7, "Final Chorus", "8", "The last chorus with full energy and sometimes a key change"),
        (8, "Outro / Tag", "4", "Short closing, sometimes repeating the song title or a final line")
    ]
    for order, name, bars, desc in country_sections:
        structures.append((country_id, name, order, bars, desc))

    # Afrobeat structure
    afro_id = genre_map["Afrobeat"]
    afro_sections = [
        (1, "Intro / Groove", "4-8", "Percussion and rhythm section establish the groove"),
        (2, "Verse 1", "8", "Vocal entry with the first narrative over the rhythmic bed"),
        (3, "Chorus", "8", "Call-and-response or singalong section with a strong hook"),
        (4, "Verse 2", "8", "Continues the story with new lyrics and vocal texture"),
        (5, "Chorus", "8", "Returns to the infectious hook section"),
        (6, "Dance Break / Solo", "8-16", "Instrumental break for dancing with percussion or horn solos"),
        (7, "Chorus", "8", "Final sing-along with maximum energy"),
        (8, "Outro / Fade", "4-8", "Gradual wind down or abrupt stop after the dance peak")
    ]
    for order, name, bars, desc in afro_sections:
        structures.append((afro_id, name, order, bars, desc))

    cursor.executemany(
        "INSERT INTO structures (genre_id, section_name, section_order, bar_count, description) VALUES (?, ?, ?, ?, ?)",
        structures
    )

    # --- rhyme schemes ---
    rhyme_data = []

    # Pop rhyme schemes
    rhyme_data.extend([
        (pop_id, "AABB", "Couplet",
         "I see you walking down the street / The way you move just can't be beat"),
        (pop_id, "ABAB", "Alternate",
         "You light up every room you're in / The stars could never shine as bright / "
         "I feel it deep beneath my skin / You make the darkness turn to light"),
        (pop_id, "XAXA", "Open Alternate",
         "Something about the way you smile / And everything just feels okay / "
         "Been thinking bout you for a while / I hope you never go away"),
    ])

    # Rock rhyme schemes
    rhyme_data.extend([
        (rock_id, "AABB", "Couplet",
         "We're burning down the city walls / We hear the thunder as it calls"),
        (rock_id, "ABAB", "Alternate",
         "The road ahead is dark and long / The engine roars beneath the hood / "
         "We're playing our defiant song / Through every wrecked and broken wood"),
        (rock_id, "AAAX", "Triple Strike",
         "We rise we fall we stand our ground / The echoes shake without a sound / "
         "We push until the lost is found / Then break the chains that held us down"),
    ])

    # Hip-Hop rhyme schemes
    rhyme_data.extend([
        (hiphop_id, "AABB", "Couplet",
         "I grind all day I never stop / Started from the bottom headed to the top"),
        (hiphop_id, "ABAB", "Alternate",
         "They said I wouldn't make it far / But look at where I'm standing now / "
         "I'm reaching for a bigger star / And making doubters take a bow"),
        (hiphop_id, "AAAA", "Monorhyme",
         "I spit the fire that you desire / Take it higher climbing every wire / "
         "Never tire I'm the one they hire / King of the empire watch the world admire"),
        (hiphop_id, "Internal", "Internal Rhyme",
         "I'm flowing and going, showing and knowing / "
         "The seeds that I'm sowing keep growing and glowing"),
    ])

    # R&B rhyme schemes
    rhyme_data.extend([
        (rnb_id, "ABAB", "Alternate",
         "Your touch it feels like summer rain / Your voice the sweetest melody / "
         "Without you I just feel the pain / Come back and lay right next to me"),
        (rnb_id, "AABB", "Couplet",
         "I hold you close beneath the moonlit sky / Together we can watch the world go by"),
        (rnb_id, "XAXA", "Open Alternate",
         "Every night I think of what we had / The memories still feel brand new / "
         "I can't pretend that I'm not sad / Cause everything reminds me of you"),
    ])

    # Country rhyme schemes
    rhyme_data.extend([
        (country_id, "ABAB", "Alternate",
         "Dirt road winding through the fields of gold / The sunset painting orange and red / "
         "These are the stories that are always told / By folks who live on love and bread"),
        (country_id, "AABB", "Couplet",
         "She picked me up in her old Chevy truck / "
         "We drove all night just trusting our luck"),
        (country_id, "XAXB", "Loose Alternate",
         "Growing up in a one-horse town / Mama always had suppertime ready / "
         "Friday nights when the sun goes down / Working hard and keeping steady"),
    ])

    # Afrobeat rhyme schemes
    rhyme_data.extend([
        (afro_id, "AABB", "Couplet",
         "We dey dance under the moonlight glow / "
         "The rhythm takes us where the rivers flow"),
        (afro_id, "ABAB", "Alternate",
         "The drums are calling from across the land / The people gather moving to the beat / "
         "Together we are stronger hand in hand / Dancing barefoot in the morning heat"),
        (afro_id, "Call-Response", "Call and Response",
         "Leader: Who go carry this load? / Response: We go carry am together / "
         "Leader: Who fit walk this road? / Response: We go walk am forever"),
    ])

    cursor.executemany(
        "INSERT INTO rhyme_schemes (genre_id, pattern, name, example) VALUES (?, ?, ?, ?)",
        rhyme_data
    )

    # --- tips ---
    tips_data = []

    # Pop tips
    tips_data.extend([
        (pop_id, "Keep your chorus lyrics simple and repetitive so they stick in the listener's head."),
        (pop_id, "Use a strong pre-chorus to build anticipation before the chorus drops."),
        (pop_id, "Write your hook first, then build the verses around it."),
        (pop_id, "Aim for a total song length of 3 to 4 minutes for radio and streaming."),
        (pop_id, "Use contrast between verse and chorus by switching up the melody or energy."),
    ])

    # Rock tips
    tips_data.extend([
        (rock_id, "Let the guitar riff be as memorable as the vocal melody."),
        (rock_id, "Don't be afraid of dynamics: go quiet in verses and loud in choruses."),
        (rock_id, "Write lyrics that feel raw and honest. Rock fans appreciate authenticity."),
        (rock_id, "Use power chords for an instant rock feel, then add complexity later."),
        (rock_id, "Leave space for an instrumental solo to show emotion without words."),
    ])

    # Hip-Hop tips
    tips_data.extend([
        (hiphop_id, "Master your flow first. The rhythm of your words is just as important as their meaning."),
        (hiphop_id, "Use internal rhymes and multi-syllable rhymes to create complex patterns."),
        (hiphop_id, "Write in 4-bar sections and build up to 16-bar verses one block at a time."),
        (hiphop_id, "Your hook should be short, catchy, and easy to remember and chant along to."),
        (hiphop_id, "Study different rappers to understand how flow speed and rhythm create different vibes."),
    ])

    # R&B tips
    tips_data.extend([
        (rnb_id, "Focus on melody and vocal delivery over complex lyrics."),
        (rnb_id, "Use smooth chord progressions like 2-5-1 or minor 7th chords for that soulful feel."),
        (rnb_id, "Add vocal runs and ad-libs in later choruses to build emotional intensity."),
        (rnb_id, "Write about specific moments and feelings rather than abstract ideas."),
        (rnb_id, "Use falsetto or head voice for emotional peaks in the bridge or final chorus."),
    ])

    # Country tips
    tips_data.extend([
        (country_id, "Tell a story with a beginning, middle, and end across your verses."),
        (country_id, "Use vivid imagery and specific details to paint pictures with your words."),
        (country_id, "Keep the melody singable, something a crowd could sing back at a concert."),
        (country_id, "Include the song title in the chorus, ideally as the first or last line."),
        (country_id, "Use conversational language. Country lyrics should sound like talking to a friend."),
    ])

    # Afrobeat tips
    tips_data.extend([
        (afro_id, "Let the groove come first. Build your melody on top of the rhythmic foundation."),
        (afro_id, "Mix languages in your lyrics if it fits. Many Afrobeat hits blend English with local languages."),
        (afro_id, "Use call-and-response patterns in your chorus for audience participation."),
        (afro_id, "Keep your melodies simple and repetitive so they become infectious earworms."),
        (afro_id, "Include a dance break section where the instrumental groove takes over."),
    ])

    cursor.executemany(
        "INSERT INTO tips (genre_id, tip_text) VALUES (?, ?)",
        tips_data
    )

    conn.commit()
