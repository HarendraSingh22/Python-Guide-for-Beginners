from __future__ import print_function
import sys

if sys.version_info[0] == 2:
    input = raw_input


def ask_for_number(prompt):
    while True:
        my_number = input(prompt)
        try:
            return float(my_number)
        except:
            continue


first = ask_for_number("Enter first number: ")
second = ask_for_number("Enter second number: ")

print("The maximum of both numbers is", max(first, second))
