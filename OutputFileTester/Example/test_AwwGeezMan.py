# Program to test the Personal Space Homework assignments

import ProgramTester as PT
import pytest, os
    
def main(filename = None):
    # Create a ProgramTester object
    pt = PT.ProgramTester("AwwGeezMan")
    # Build the program
    pt.build_program()
    
    # Test the program with a given filename
    if filename == None:
    	filename = "output_0.txt" # Change this to test another file
    pt.test_program(filename) 

# Parameterize the python test object with the 15 output files to test against    
@pytest.mark.parametrize('input', ["output_{}.txt".format(i) for i in range(1, 77)])    
def test_submission(input):
    # Create a ProgramTester object
    pt = PT.ProgramTester("AwwGeezMan")
    # Test the program with the program tester object
    assert pt.test_program(input)
    
# Provide main if students want to test each file individually
if __name__ == "__main__":
    main("output_0.txt") # Change this to test against another file if needed