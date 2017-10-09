import sys

# Program to print Pascal's Triangle in Python

# asks user for input
number_of_rows = input("How tall do you want your Pascal's triangle?\n")

# converts user input to a number, error if cannot
number_of_rows = int(number_of_rows)

# makes sure user number is above 0, error if not
assert(number_of_rows > 0)

current_number = 1
for i in range(number_of_rows):
    for j in range(i):
        # print the current number with no space at the end
        # checks which python version you have and prints with that in mind
        print(str(current_number), end=" ") if (sys.version_info > (3,0)) else print(str(current_number), )
        current_number = current_number + 1
    print()

