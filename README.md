# SongCraft

A command-line songwriting guide tool that helps artists understand song structures, rhyme schemes, and writing techniques across different music genres.

## Team Members

- Member 1 — _[Name]_
- Member 2 — _[Name]_
- Member 3 — _[Name]_
- Member 4 — _[Name]_
- Member 5 — _[Name]_

## About

SongCraft is a menu-driven Python application that walks you through the process of writing a song. You pick a topic (what you want to sing about), choose a genre, and the tool gives you:

- The recommended **song structure** (intro, verse, chorus, bridge, etc.) with bar counts
- Common **rhyme schemes** used in that genre with examples
- Practical **songwriting tips** specific to that genre

The application stores all its data in a **SQLite database** and supports 6 genres: Pop, Rock, Hip-Hop, R&B, Country, and Afrobeat.

## How to Run

### Requirements

- Python 3.6 or higher

### Quick Start

```bash
# on Linux / macOS
chmod +x run.sh
./run.sh

# on Windows
python main.py
```

### Setup (optional)

If you want to reset the database:

```bash
chmod +x setup.sh
./setup.sh
```

## Project Structure

```
songcraft-cli/
├── main.py              # Entry point
├── setup.sh             # Database setup script
├── run.sh               # Run script
├── requirements.txt     # Dependencies
├── db/
│   ├── __init__.py
│   ├── connection.py    # Database connection
│   ├── schema.py        # Table definitions
│   └── seed.py          # Data population
└── app/
    ├── __init__.py
    ├── menu.py           # Menu navigation
    ├── guide.py          # Songwriting guide flow
    └── display.py        # Output formatting
```

## Features

- Browse available music genres and their descriptions
- Browse common song topics (Love, Heartbreak, Celebration, etc.)
- Get a full songwriting guide for any genre + topic combination
- View detailed song structure with section names and bar counts
- Learn rhyme scheme patterns with examples
- Read genre-specific songwriting tips
- Save your guide summary to a text file
