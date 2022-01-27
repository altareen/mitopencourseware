###
#-------------------------------------------------------------------------------
# test_problem3.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the problem3.py code.
#
##

from problem3 import longest
import pytest

@pytest.mark.parametrize('s, expected', [
    ('azcbobobegghakl', 'Longest substring in alphabetical order is: beggh'),
    ('abcbcd', 'Longest substring in alphabetical order is: abc'),
    ('ddqffwrmc', 'Longest substring in alphabetical order is: ddq'),
    ('ucytbmbv', 'Longest substring in alphabetical order is: cy'),
    ('mmjxxjlwbsztw', 'Longest substring in alphabetical order is: jxx'),
    ('fsodrequsmfhflqcjzqy', 'Longest substring in alphabetical order is: equ'),
    ('omytrootbfilzqyvdseibx', 'Longest substring in alphabetical order is: bfilz'),
    ('rkhrzaasubsehowckx', 'Longest substring in alphabetical order is: aasu'),
    ('nbirygaamcpzwnjuyujwgvj', 'Longest substring in alphabetical order is: biry'),
    ('abcdefghijklmnopqrstuvwxyz', 'Longest substring in alphabetical order is: abcdefghijklmnopqrstuvwxyz'),
    ('hpxwkxyxycwdvjihhwjfaohx', 'Longest substring in alphabetical order is: hpx'),
    ('tmvfdrqqjmtlird', 'Longest substring in alphabetical order is: jmt'),
    ('vxnsnzokzbmiqgdqpas', 'Longest substring in alphabetical order is: vx'),
    ('zyxwvutsrqponmlkjihgfedcba', 'Longest substring in alphabetical order is: z'),
    ('eydvrxcdasqa', 'Longest substring in alphabetical order is: ey'),
    ('tjfjcbwmu', 'Longest substring in alphabetical order is: fj'),
    ('ejgyunlujy', 'Longest substring in alphabetical order is: ej'),
    ('zxhzomcpeugrjxaatqcbsxbn', 'Longest substring in alphabetical order is: aat'),
    ('dlqavpkbd', 'Longest substring in alphabetical order is: dlq'),
    ('wendifuqrnby', 'Longest substring in alphabetical order is: en'),
    ('djtlswyttluvwrkul', 'Longest substring in alphabetical order is: lswy'),
    ('huwucfzuw', 'Longest substring in alphabetical order is: huw'),
])

def test_result(s, expected):
    actual = longest(s)
    assert actual == expected
