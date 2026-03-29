# SongCraft CLI (PLP-2)

A professional-grade command-line songwriting laboratory that leverages **Data Science** and **Cloud Infrastructure** to help artists master their craft.

## Team Role Assignments (GitHub Contributions)

- **Member 1 (Don):** Principal Algorithm Architect (Pattern Matcher)
- **Member 2 (Malaika):** Database Security & User Profile Systems
- **Member 3 (Gihoza):** CRUD & Application Navigation Logic
- **Member 4 (Ishimwe):** Songwriting Assistant & Content Logic
- **Member 5 (Berthe):** Core Application Shell & Database Schema

## Major PLP-2 Upgrades

### Style DNA Pattern Matcher
Our standout feature. The app extracts a writing "fingerprint" from raw text-analyzing **Rhyme Density**, **Syllable Tempo**, and **Vocabulary Richness**. It matches the user's style against a database of 20+ legendary artists using the **Cosine Similarity** algorithm (Vector Mathematics).

### Cloud Persistence (Aiven MySQL)
Migrated from localized SQLite to a professional **Aiven MySQL** cloud database. This enables team-wide data synchronization and secure SSL-encrypted connections.

### Profiles & Gamification
A custom RPG-style leveling system. Every song draft or style analysis awards **XP**. 
- **Level Formula:** `Floor(1 + √XP/50)`
- Tracks user streaks and progression levels in the cloud.

### Full Library Management (CRUD)
Complete administrative control over the database. Users can Create, Read, Update, and Delete Genres, Topics, Tips, and personal Song Drafts.

## Tech Stack

- **Core:** Python 3.x
- **Database:** MySQL 8.0 (Aiven Cloud)
- **Encryption:** SSL-enabled database connections
- **Algorithm:** Vector-based Cosine Similarity
- **Dependencies:** `mysql-connector-python`

## How to Run

```bash
# Initialize & Run (Unix/Mac)
chmod +x setup.sh run.sh
./run.sh

# Run (Windows)
python main.py
```

## Project Structure

```
songcraft-cli/
├── main.py              # Application Entry & Unicode Encoding Fixes
├── db/
│   ├── connection.py    # SSL Cloud Database Bridge
│   ├── schema.py        # Normalized Relational Schema
│   └── seed.py          # Data Population (Artist Vectors & Genres)
└── app/
    ├── pattern_matcher.py # Mathematical Content Analysis Engine
    ├── user.py           # Login & XP/Leveling Gamification
    ├── crud.py           # Library Management System
    ├── guide.py          # Interactive Writing Assistant
    └── display.py        # ASCII Terminal Rendering Engine
```
