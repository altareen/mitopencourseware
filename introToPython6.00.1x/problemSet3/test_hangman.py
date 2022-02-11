###
#-------------------------------------------------------------------------------
# test_hangman.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 10, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the ps3_hangman.py code.
#
##

from ps3_hangman import *
import pytest

@pytest.mark.parametrize('secretWord, lettersGuessed, expected', [
    ('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'], False),
    ('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'], True),
    ('banana', ['e', 'f', 'x', 'm', 'p', 's', 'd', 'a', 'b', 'w'], False),
    ('lettuce', ['j', 'y', 'f', 'p', 'u', 'h', 'v', 'o', 'q', 'z'], False),
    ('coconut', [], False),
    ('carrot', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't'], True),
])

def test_isWordGuessed(secretWord, lettersGuessed, expected):
    actual = isWordGuessed(secretWord, lettersGuessed)
    assert actual == expected

#--------------------------------------

@pytest.mark.parametrize('secretWord, lettersGuessed, expected', [
    ('apple', ['e', 'i', 'k', 'p', 'r', 's'], '_pp_e'),
    ('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'], 'durian'),
    ('banana', ['p', 'e', 'x', 'g', 'h', 'c', 'r', 'y', 'l', 'd'], '______'),
    ('pineapple', ['t', 'i', 'n', 'v', 's', 'z', 'b', 'h', 'y', 'k'], '_in______'),
    ('banana', [], '______'),
    ('pineapple', ['a', 'y', 'r', 'q', 'h', 'n', 'o', 'v', 'g', 'i'], '_in_a____'),
])

def test_getGuessedWord(secretWord, lettersGuessed, expected):
    actual = getGuessedWord(secretWord, lettersGuessed)
    assert actual == expected

#--------------------------------------

@pytest.mark.parametrize('lettersGuessed, expected', [
    (['e', 'i', 'k', 'p', 'r', 's'], 'abcdfghjlmnoqtuvwxyz'),
    ([], 'abcdefghijklmnopqrstuvwxyz'),
    (['g'], 'abcdefhijklmnopqrstuvwxyz'),
    (['z', 'f', 'd', 'w', 'l', 'b', 'x', 'i', 's', 'o'], 'aceghjkmnpqrtuvy'),
    (['j', 'b', 'e', 'i', 'd', 'a', 'x'], 'cfghklmnopqrstuvwyz'),
    (['w', 'y'], 'abcdefghijklmnopqrstuvxz'),
])

def test_getAvailableLetters(lettersGuessed, expected):
    actual = getAvailableLetters(lettersGuessed)
    assert actual == expected
