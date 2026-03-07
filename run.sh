#!/bin/bash

# check python
if command -v python3 &> /dev/null; then
    PY=python3
elif command -v python &> /dev/null; then
    PY=python
else
    echo ""
    echo "  ERROR: Python is not installed."
    echo "  Please install Python 3.6 or higher to run SongCraft."
    echo ""
    exit 1
fi

$PY main.py
