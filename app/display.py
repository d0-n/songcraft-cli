def print_header(text):
    width = len(text) + 6
    print()
    print("  " + "=" * width)
    print("  |  " + text + "  |")
    print("  " + "=" * width)
    print()


def print_divider():
    print("  " + "-" * 40)


def show_structure(sections):
    print_header("SONG STRUCTURE")
    print("  Below is the recommended structure for this genre.\n")
    for i, section in enumerate(sections):
        name = section["section_name"]
        bars = section["bar_count"]
        desc = section["description"]
        print(f"  {i + 1}. {name} ({bars} bars)")
        print(f"     {desc}")
        print()
    print_divider()


def show_rhyme_schemes(schemes):
    print_header("RHYME SCHEMES")
    print("  Common rhyme patterns used in this genre.\n")
    for scheme in schemes:
        name = scheme["name"]
        pattern = scheme["pattern"]
        example = scheme["example"]
        print(f"  >> {name} ({pattern})")
        print(f"     Example: {example}")
        print()
    print_divider()


def show_tips(tips):
    print_header("SONGWRITING TIPS")
    print("  Helpful tips for writing in this genre.\n")
    for i, tip in enumerate(tips):
        text = tip["tip_text"]
        print(f"  {i + 1}. {text}")
    print()
    print_divider()


def show_genre_info(genre):
    name = genre["name"]
    desc = genre["description"]
    print(f"\n  Genre: {name}")
    print(f"  {desc}")
    print()


def show_topic_info(topic):
    name = topic["name"]
    desc = topic["description"]
    print(f"\n  Topic: {name}")
    print(f"  {desc}")
    print()
