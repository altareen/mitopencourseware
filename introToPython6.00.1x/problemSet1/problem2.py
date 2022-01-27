###
#-------------------------------------------------------------------------------
# problem2.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2022
# Execution:    python3 problem2.py
#
# This program counts the number of times 'bob' appears in a string.
#
##

def countbobs(s):
    count = 0
    for i in range(0, len(s)-2):
        chunk = s[i:i+3]
        if chunk == 'bob':
            count += 1
    return f'Number of times bob occurs is: {count}'

result = countbobs('azcbobobegghakl')
print(result)
