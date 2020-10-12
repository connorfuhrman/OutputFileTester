import ProgramTester as PT
import pytest, os

# Build the program once before entering pytest
def pytest_configure():
    os.chdir("Tester")
    # Create a ProgramTester object
    pt = PT.ProgramTester("AwwGeezMan")
    # Build the user's program 
    pt.build_program()