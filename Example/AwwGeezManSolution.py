# Program to generate solution files for the PersonalSpace homework assignment

import ProgramTester as PT
import os, shutil
import random
    
def main():
    # Create a ProgramTester object
    pt = PT.ProgramTester("AwwGeezMan")
    # Build the program (the solution)
    pt.build_program()
    
    # Create the solution directory
    try:
        os.mkdir("solution")
    except:
        shutil.rmtree("solution")
        os.mkdir("solution")
    
    # Define what command line arguments we want to test with
    arguments = []
    # Test the most basics cases
    print("Generating the simble base cases")
    for dim in ["C137", "Z286"]:
    	arguments.append("1 30 {}".format(dim))
    
    # Use the ./AwwGeezMan {start} {stop} {dimension} for various start and stops
    print("Generating for various start/stop")
    for stop in range(25, 51):
    	start = random.randint(1, stop - 1)
    	arguments.append("{} {} C137".format(start, stop))
    	arguments.append("{} {} Z286".format(start, stop))
    # Now tests the ./AwwGeezMan {start} {stop} {step} {dimension}
    print("Generating tests for different delta's")
    stop = 50
    for d in range(2, 11):
    	start = random.randint(1, stop - 1)
    	arguments.append("{} {} {} C137".format(start, stop, d))
    	arguments.append("{} {} {} Z286".format(start, stop, d))
    
    # Test for a very long range
    arguments.append("10 100 C137")
    arguments.append("50 5000 4 Z286")
    
    # Test for bogus dimensions
    arguments.append("10 100 Dfadsf")
    arguments.append("10 100 adfa")
    arguments.append("10 100 afdasfea")
    
    # Generate the solution files
    for i, a in enumerate(arguments):
        # Run the program with the given arguments
        out = pt.execute_program(a)
        f = open("{}/output_{}.txt".format(pt.solution_dir, i), 'w')
        f.write("# Command arguments: {}\n# Solution:\n".format(a))
        for l in out:
            f.write("{}\n".format(l))
        f.close()
    # Write the command line arguments to a file for reproducability
    f = open("{}/command_arguments.txt".format(pt.solution_dir, i), 'w')
    s = ""
    for i, a in enumerate(arguments):
        s += "[args for output_{}.txt] {}\n".format(i, a)
    f.write(s)
    f.close()

    
if __name__ == "__main__":
    main() 