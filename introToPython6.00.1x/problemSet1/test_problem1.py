###
#-------------------------------------------------------------------------------
# test_problem1.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the problem1.py code.
#
##

from problem1 import vowels
import pytest

@pytest.mark.parametrize('s, expected', [
    ('azcbobobegghakl', 'Number of vowels: 5'),
    ('ildoiiozwsgvalyyp', 'Number of vowels: 6'),
    ('zuuigxulaoseukhmyuvx', 'Number of vowels: 9'),
    ('rmdrnofuubgskvexeouz', 'Number of vowels: 7'),
    ('uskzuknecungnwagspyz', 'Number of vowels: 5'),
    ('tsuekekdmiojuheedmwfhyti', 'Number of vowels: 9'),
    ('hqoohrieoza', 'Number of vowels: 6'),
    ('btvnyffkeuswo', 'Number of vowels: 3'),
    ('ppeihoanglume', 'Number of vowels: 6'),
    ('ljftrrafxqimokueqe', 'Number of vowels: 6'),
    ('emjnivyipghesbajmcsusow', 'Number of vowels: 7'),
    ('buwvug', 'Number of vowels: 2'),
    ('hjlmah', 'Number of vowels: 1'),
    ('lodguamikjk', 'Number of vowels: 4'),
    ('wpbucaourbj', 'Number of vowels: 4'),
    ('gtxwanyiiwjged', 'Number of vowels: 4'),
    ('unxaeeneesqvig', 'Number of vowels: 7'),
    ('racxepn', 'Number of vowels: 2'),
    ('nndtourgolz', 'Number of vowels: 3'),
    ('qoudpjgwzieoruqxo', 'Number of vowels: 7'),
    ('tkesxirtesozpgwpaietbevi', 'Number of vowels: 9'),
])

def test_result(s, expected):
    actual = vowels(s)
    assert actual == expected
