#!/usr/bin/python3
import sys

# Get the number of arguments
num_args = len(sys.argv) - 1  # The first element in sys.argv is the script name

# Print the number of arguments
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

# Print the list of arguments
for i in range(1, num_args + 1):
    print("{}: {}".format(i, sys.argv[i]))