###
#-------------------------------------------------------------------------------
# problem3.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2022
# Execution:    python3 problem3.py
#
# This program displays the longest substring in which the letters occur in
# alphabetical order.
#
##

def longest(s):
    result = ''
    for i in range(len(s)-1):
        for j in range(i, len(s)):
            chunk = s[i:j+1]
            if list(chunk) == sorted(chunk) and len(chunk) > len(result):
                result = chunk
    return f'Longest substring in alphabetical order is: {result}'
