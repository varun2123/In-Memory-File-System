#!/bin/bash

# Run unit tests
echo "Running unit tests..."
python3 -m unittest discover -s tests

# Start the interactive CLI
echo "Starting interactive CLI..."
python3 src/cli.py
