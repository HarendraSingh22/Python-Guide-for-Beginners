#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:23:49 2017

@author: cam-barts
"""
import argparse
# Using argparse, which is a argument parsing module from the standard library, to take input from the user
# https://docs.python.org/2/library/argparse.html
parser = argparse.ArgumentParser()

# Create an agrument, named 'String' and will be accessed as args.String. It will be of string type, and the help block with say "String to check palindrome-ness"
# $python palindrome.py -h
# usage: palindrome.py [-h] <string>
#
# positional arguments:
#  <sring>           String to check palindrome-ness
parser.add_argument("String", type=str, help= "String to check palindrome-ness")
args = parser.parse_args()
String = args.String

# Adding [::-1] reverses a string in python2
StringReverse = String[::-1]

if __name__ == '__main__':
    if str(String) == str(StringReverse):
        print "String is a palindrome!"
    else:
        print "String is not a palindrome!"
