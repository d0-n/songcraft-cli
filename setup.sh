#!/bin/bash

echo ""
echo "  SongCraft - Database Setup"
echo "  =========================="
echo ""

# check python
if command -v python3 &> /dev/null; then
    PY=python3
elif command -v python &> /dev/null; then
    PY=python
else
    echo "  ERROR: Python is not installed."
    echo "  Please install Python 3.6 or higher."
    exit 1
fi

echo "  Using: $($PY --version)"
echo ""

# remove old database if it exists
if [ -f "songcraft.db" ]; then
    echo "  Removing old database..."
    rm songcraft.db
fi

# run setup
echo "  Creating database and seeding data..."
$PY -c "
from db.connection import get_connection
from db.schema import create_tables
from db.seed import seed_data

conn = get_connection()
create_tables(conn)
seed_data(conn)
conn.close()
print('  Done! Database is ready.')
"

echo ""
echo "  Setup complete. Run ./run.sh to start SongCraft."
echo ""
