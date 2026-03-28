def print_header(text):
    """Print a formatted section header."""
    width = len(text) + 6
    print()
    print("  " + "=" * width)
    print("  |  " + text + "  |")
    print("  " + "=" * width)
    print()


def print_divider():
    """Print a horizontal divider line."""
    print("  " + "-" * 40)


def show_structure(sections):
    """Display song structure with ASCII bar visualization."""
    print_header("SONG STRUCTURE")
    print("  Below is the recommended structure for this genre.\n")
    for i, section in enumerate(sections):
        name = section[0]       # section_name
        bars = section[2]       # bar_count
        desc = section[3]       # description
        print(f"  {i + 1}. {name} ({bars} bars)")
        print(f"     {desc}")
        print()

    # ASCII bar chart visualizer
    print_divider()
    print_header("STRUCTURE VISUALIZER")
    for section in sections:
        name = section[0]
        bars = section[2]
        # Convert bar_count to a number for the chart
        try:
            bar_num = int(bars.split("-")[0])
        except (ValueError, AttributeError):
            bar_num = 4
        bar_visual = "█" * (bar_num * 2)
        label = name.ljust(20)
        print(f"  {label} {bar_visual} ({bars} bars)")
    print()
    print_divider()


def show_rhyme_schemes(schemes):
    """Display rhyme scheme patterns with examples."""
    print_header("RHYME SCHEMES")
    print("  Common rhyme patterns used in this genre.\n")
    for scheme in schemes:
        name = scheme[1]        # name
        pattern = scheme[0]     # pattern
        example = scheme[2]     # example
        print(f"  >> {name} ({pattern})")
        print(f"     Example: {example}")
        print()
    print_divider()


def show_tips(tips):
    """Display songwriting tips."""
    print_header("SONGWRITING TIPS")
    print("  Helpful tips for writing in this genre.\n")
    for i, tip in enumerate(tips):
        text = tip[0]           # tip_text
        print(f"  {i + 1}. {text}")
    print()
    print_divider()


def show_genre_info(genre):
    """Display info about a selected genre."""
    name = genre[1]             # name
    desc = genre[2]             # description
    print(f"\n  Genre: {name}")
    print(f"  {desc}")
    print()


def show_topic_info(topic):
    """Display info about a selected topic."""
    if isinstance(topic, dict):
        name = topic["name"]
        desc = topic["description"]
    else:
        name = topic[1]
        desc = topic[2]
    print(f"\n  Topic: {name}")
    print(f"  {desc}")
    print()
