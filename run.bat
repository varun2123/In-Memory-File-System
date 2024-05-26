@echo off
echo Running unit tests...
python -m tests.test_file_system
echo Finished running unit tests

echo Starting interactive CLI...
python -m src.cli
echo Started interactive CLI
