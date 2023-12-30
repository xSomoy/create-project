# Python program to demonstrate
# command line arguments


import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
for i in sys.argv:
    print(i)
