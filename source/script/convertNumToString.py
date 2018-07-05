#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import re

# Function to convert number into char
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        "0": "khoong",
        "1": "moojt",
        "2": "hai",
        "3": "ba",
        "4": "boosn",
        "5": "nawm",
        "6": "sasu",
        "7": "bary",
        "8": "tasm",
        "9": "chisn",
    }
    return switcher.get(argument, "nothing")

# Preparing the file
f_input  = open(sys.argv[1], "r", encoding="utf-8")
f_output = open(sys.argv[2], "w", encoding="utf-8")

# Read file input 
line = f_input.read()
result = ""

for letter in line:
	char = numbers_to_strings(letter);
	if char != "nothing":
		result += char + "\n"


f_output.write(result)
f_output.write("\n")

# Closing the file
f_input.close()
f_output.close()