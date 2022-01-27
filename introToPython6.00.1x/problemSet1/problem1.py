###
#-------------------------------------------------------------------------------
# problem1.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2022
# Execution:    python3 problem1.py
#
# This program counts the number of vowels contained in a string.
#
##

def vowels(s):
    count = 0
    for letter in s:
        if letter in 'aeiou':
            count += 1
    return f'Number of vowels: {count}'
