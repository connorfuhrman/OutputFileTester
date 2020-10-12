# Defines a class to test a program for ECE 275

import os, shutil, subprocess, difflib, re
from pprint import pprint
import pytest


class ProgramTester:
    def __init__(self, executable_name):
        # Set the object member variables
        self.test_build_dir = "testingBuild"
        self.solution_dir = "solution"
        self.executable_name = "src/" + executable_name
        
    def build_program(self):    
        try:
            # Try to make the directory
            os.mkdir(self.test_build_dir)
        except: 
            # If we get an error then it already exists
            print("The build directory already exists. Deleting and creating anew")
            shutil.rmtree(self.test_build_dir)
            os.mkdir(self.test_build_dir)
        # Move to the directory we just created
        os.chdir(self.test_build_dir)
        command = 'cmake ../..'
        print("Executing the cmake command to generate build files:")
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error == None:
            print("CMake command executed correctly with the following output:")
            print(output.decode("utf-8") )
        else:
            print("CMake encountered the following error\n {}\n\nContact the instructor.".format(error.decode("utf-8") ))
        print("Building the program now ")
        command = "make all"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error == None:
            print("Build executed correctly with the following output:")
            print(output.decode("utf-8") )
        else:
            print("Build encountered the following error: {}.".format(error.decode("utf-8")))
        # Move back to the working dir
        os.chdir("../")
        
    def execute_program(self, command_arguments = None):
        print("Executing program {} with the following arguments: {}".format(self.executable_name, command_arguments))
        if command_arguments == None:
            command = "./{}/{}".format(self.test_build_dir, self.executable_name)
        else:
            command = "./{}/{} {}".format(self.test_build_dir, self.executable_name, command_arguments)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error != None:
            print("There was the following error in the program: \n{}".format(error.decode("utf-8")))
        # Return the lines and don't care about whitespace lines
        output = output.decode("utf-8")
        lines = []
        for l in output.splitlines():
            if len(l) != 0:
                lines.append(l)
        return lines
        
    def read_output_file(self, filename):
        ''' Returns a list where each entry is one line of the file given by filename. No lines that are only
        whitespace are returned. '''
        with open(filename) as f:
            # Read the data from the file
            file_data = f.read()
            # Split into all the lines
            lines_tmp = file_data.splitlines()
            lines = []
            # Don't keep the lines that start with a comment
            for l in lines_tmp:
                # Strip leading and lagging whitespace
                l.strip()
                try:
                    if l[0] != "#": lines.append(l)
                except: # Then l is a newline character and we don't really care about those.
                    pass 
        return lines
    
    def get_command_arguments(self, solution_filename):
        ''' Read the command line arguments from the solution file and return so that
        we can execute the program with those command line arguments'''
        with open("solution/{}".format(solution_filename)) as f:
            # Get the first line in the file
            line = f.readline()
            # And strip the "# Command arguments: " from the string
            args = re.sub("# Command arguments: ", '', line)
        return args
            
    def compare_output(self, program_out, solution_out):
        d = difflib.Differ()
        result = list(d.compare(program_out, solution_out))
        matches_solution = True
        for r in result: # Loop through the comparisons
            if not r[0] == " ":
                matches_solution = False
        if not matches_solution:
            print("[F] Your program does not match the solution!! See below:")
            for r in result:
                print(r)
        else:
            print("[S] Your program matches the solution!!")
        return matches_solution 
        
    def test_program(self, solution_filename):
        # Execute the program
        out = self.execute_program(self.get_command_arguments(solution_filename))
        return self.compare_output(out, self.read_output_file("solution/{}".format(solution_filename)))