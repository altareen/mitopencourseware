###
#-------------------------------------------------------------------------------
# test_problem2.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the problem2.py code.
#
##

from problem2 import countbobs
import pytest

@pytest.mark.parametrize('s, expected', [
    ('azcbobobegghakl', 'Number of times bob occurs is: 2'),
    ('bobbnmobooobobobobobobobqbmboebobbbboobobobobooboobobo', 'Number of times bob occurs is: 12'),
    ('sbobobobooboboboobobo', 'Number of times bob occurs is: 6'),
    ('bobobboobobobboboblboobo', 'Number of times bob occurs is: 6'),
    ('oboboobobbobbjbobobfbobb', 'Number of times bob occurs is: 6'),
    ('obooobobozbobbwibobbobooxbobbbobobobobb', 'Number of times bob occurs is: 9'),
    ('obujmxpbobboboobobbdbobobobbobot', 'Number of times bob occurs is: 7'),
    ('obobqbuabolbgoobooobobbobbbooboboboobb', 'Number of times bob occurs is: 5'),
    ('yvyptofrnqx', 'Number of times bob occurs is: 0'),
    ('bobobobobobobobobobob', 'Number of times bob occurs is: 10'),
    ('koboboboobsyboobtg', 'Number of times bob occurs is: 2'),
    ('obobzobbolbbobbobbondmbobob', 'Number of times bob occurs is: 5'),
    ('oboooboobobobbobbohofo', 'Number of times bob occurs is: 3'),
    ('hobooroxz', 'Number of times bob occurs is: 0'),
    ('ooboboobobbobobbobbbobbvbobb', 'Number of times bob occurs is: 7'),
    ('hdbobobbobbbobobobooboobobbx', 'Number of times bob occurs is: 7'),
    ('bobboboobobooobobdboboboobobbooboobobbobobcoboobbobobbobb', 'Number of times bob occurs is: 13'),
    ('bobboboobxtobobboobabobboobbobbfiobobo', 'Number of times bob occurs is: 6'),
    ('boboobobobboubobbobobobadbobbobb', 'Number of times bob occurs is: 9'),
    ('obqkobobbobobooboooboboobobbobobtkob', 'Number of times bob occurs is: 7'),
    ('obbobbobobobt', 'Number of times bob occurs is: 4'),
])

def test_result(s, expected):
    actual = countbobs(s)
    assert actual == expected
