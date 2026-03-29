# SongCraft CLI (PLP-2)

A command-line songwriting tool that uses **Cloud Database** storage and **Data Science** to help artists improve their craft.

## Team Role Assignments (GitHub Contributions)

- **Member 1 (Don):** Pattern Matcher Algorithm & Data Seeding
- **Member 2 (Malaika):** User Profiles, Display Logic & Database Connection
- **Member 3 (Gihoza):** CRUD Operations, Menu Navigation & Setup Script
- **Member 4 (Ishimwe):** Songwriting Guide & Dependencies
- **Member 5 (Berthe):** Main Application Entry & Database Schema

## Prerequisites

Before running SongCraft, make sure you have:

1. **Python 3.6 or higher** installed on your computer.
   - Check by running: `python --version` or `python3 --version`
   - Download from: https://www.python.org/downloads/

2. **mysql-connector-python** library.
   - Install by running:
   ```bash
   pip install mysql-connector-python
   ```
   Or on Mac/Linux:
   ```bash
   pip3 install mysql-connector-python
   ```

3. **Internet connection** (the database is hosted in the cloud).

## Database Configuration

SongCraft uses a cloud-hosted **Aiven MySQL** database. For security, the database password is **not** stored directly in the source code.

### Setting Up the Password
Create a file called `db/config.py` in the project and add this one line:
```python
DB_PASSWORD = "your_password_here"
```
This file is listed in `.gitignore` so it will not be pushed to GitHub.

### Setting Up Your Own Database (Optional)
If you want to connect to your own MySQL instance instead of the shared one:
1. Go to https://aiven.io and create a free account.
2. Create a new **MySQL** service (the free tier works fine).
3. Copy your **Host**, **Port**, **Username**, and **Password** from the Aiven dashboard.
4. Open `db/connection.py` and update the `DB_HOST`, `DB_PORT`, `DB_USER` values to match your service.
5. Add your password to `db/config.py` as shown above.
6. Run the app - it will automatically create all tables and populate the database on first launch.

## How to Run

**Windows:**
```bash
python main.py
```

**Mac / Linux:**
```bash
python3 main.py
```

### Shell Scripts (Mac / Linux only)

We provide two helper scripts for convenience:

- **`setup.sh`** - Resets and rebuilds the database from scratch. Use this if the database gets corrupted or you want a fresh start. It deletes the old data, recreates all tables, and repopulates everything.
  ```bash
  chmod +x setup.sh
  ./setup.sh
  ```

- **`run.sh`** - A quick launcher that detects your Python version and starts the app. No need to remember whether your system uses `python` or `python3`.
  ```bash
  chmod +x run.sh
  ./run.sh
  ```

> **Note:** `setup.sh` is only needed for a manual reset. On normal launches, `main.py` automatically creates tables and populates data if the database is empty.

The app will automatically:
- Connect to the cloud database
- Create all necessary tables (if they do not exist)
- Populate starter data on first launch (genres, artists, tips)
- Prompt you to log in or create a profile

## Major Features

### Pattern Matcher
The app extracts a writing "fingerprint" from your lyrics by analyzing **Rhyme Density**, **Syllable Tempo**, and **Vocabulary Richness**. It then matches your style against 20+ legendary artists using the **Cosine Similarity** algorithm.

### Cloud Persistence (Aiven MySQL)
All data is stored in a cloud MySQL database with **SSL encryption**. Your songs, profiles, and progress are synchronized remotely.

### Profiles & Gamification
A leveling system that rewards you with **XP** for writing songs and analyzing lyrics.
- **Level Formula:** `Floor(1 + √(XP / 50))`

### Library Management (CRUD)
Full control over the database. Create, Read, Update, and Delete genres, topics, tips, and personal song drafts. Your drafts are private and tied to your user profile.

## Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL 8.0 (Aiven Cloud)
- **Encryption:** SSL-enabled connections
- **Algorithm:** Vector-based Cosine Similarity
- **Dependency:** `mysql-connector-python`

## Project Structure

```
songcraft-cli/
├── main.py              # App entry point and Unicode fix
├── requirements.txt     # Python dependencies
├── db/
│   ├── __init__.py      # Marks db/ as a Python package
│   ├── config.py        # Local-only password file (not in GitHub)
│   ├── connection.py    # Cloud database connection (SSL)
│   ├── schema.py        # Table definitions
│   └── seed.py          # Starter data (genres, artists, tips)
└── app/
    ├── __init__.py      # Marks app/ as a Python package
    ├── pattern_matcher.py # Style analysis algorithm
    ├── user.py           # Login and XP/leveling system
    ├── crud.py           # Data management (Create, Read, Update, Delete)
    ├── guide.py          # Step-by-step songwriting assistant
    └── display.py        # Terminal UI formatting
```
