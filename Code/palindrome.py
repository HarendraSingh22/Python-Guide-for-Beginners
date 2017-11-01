#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:23:49 2017

@author: TheKingOfShade
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("String", type=str, help= "String to check palindrome-ness")
args = parser.parse_args()
String = args.String

StringReverse = String[::-1]

if __name__ == '__main__':
    if str(String) == str(StringReverse):
        print "String is a palindrome!"
    else:
        print "String is not a palindrome!"

