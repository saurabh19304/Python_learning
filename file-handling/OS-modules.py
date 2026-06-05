# OS module provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.

#1 Handling the current working directorty 
# The Current Working Directory (CWD) is the folder where Python is currently operating 

# Getting Current Working Directory: To get the location of the current working directory, the os.getcwd() function from the os module is used. The following code prints the current working directory (CWD).

import os 
cwd = os.getcwd()
print("Current working directory:", cwd)

# Changing Current Working Directory: It can be changed using os.chdir(path), which switches Python’s context to the specified directory. The following code prints the CWD before and after changing it one level up using os.chdir('../').

import os 
cwd = os.getcwd()
print("Current working directory:", cwd)

# Changing Current Working Directory: It can be changed using os.chdir(path), which switches Python’s context to the specified directory. The following code prints the CWD before and after changing it one level up using os.chdir('../').
