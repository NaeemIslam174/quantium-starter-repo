#!/bin/bash

# Activate the virtual environment (works on both Windows Git Bash and Mac/Linux)
if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Could not find virtual environment activation script"
    exit 1
fi

# Run the test suite
pytest test_app.py
exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "All tests passed ✓"
    exit 0
else
    echo "Some tests failed ✗"
    exit 1
fi