from __future__ import print_function
import sys

if sys.version_info[0] == 2:
    input = raw_input

my_list = ["apple", "banana", "orange", "kiwi"]

print("the list contains:")
print(repr(my_list))
needle = input("What are you looking for: ")

if needle in my_list:
    print(needle, "is part of the list")
else:
    print(needle, "is not part of the list")
