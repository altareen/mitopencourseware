###
#-------------------------------------------------------------------------------
# test_ps4a_wordgame.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 28, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the ps4a_wordgame.py code.
#
##

from ps4a_wordgame import *
import pytest

#--------------------------------------
# test bench for getWordScore
#--------------------------------------

@pytest.mark.parametrize('word, n, expected', [
    ('', 7, 0),
    ('it', 7, 4),
    ('was', 7, 18),
    ('scored', 7, 54),
    ('waybill', 7, 155),
    ('outgnaw', 7, 127),
    ('fork', 7, 44),
    ('fork', 4, 94),
    ('', 10, 0),
    ('qi', 7, 22),
    ('was', 7, 18),
    ('outgnaw', 7, 127),
    ('triplet', 7, 113),
    ('triplet', 8, 63),
    ('dogs', 4, 74),
    ('cats', 7, 24),
    ('kids', 5, 36),
    ('onomatopoeia', 12, 242),
])

def test_getWordScore(word, n, expected):
    actual = getWordScore(word, n)
    assert actual == expected

#--------------------------------------
# test bench for updateHand
#--------------------------------------

@pytest.mark.parametrize('hand, word, expected', [
    ({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, 'quail', {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}),
    ({'e':1, 'v':2, 'n':1, 'i':1, 'l':2}, 'evil', {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}),
    ({'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'hello', {'h': 0, 'e': 0, 'l': 0, 'o': 0}),
    ({'l': 2, 'a': 2, 'p': 3, 't': 2, 'c': 2, 'r': 2}, 'claptrap', {'l': 1, 'c': 1, 'r': 1, 'p': 1, 'a': 0, 't': 1}),
    ({'d': 1, 'o': 1, 'g': 1}, 'dog', {'d': 0, 'g': 0, 'o': 0}),
    ({'q': 3, 'o': 3, 'p': 3, 't': 3, 'w': 3, 'i': 3, 'y': 3, 'r': 3, 'u': 3, 'e': 3}, 'typewriter', {'u': 3, 'y': 2, 'p': 2, 'q': 3, 'e': 1, 'o': 3, 'w': 2, 'r': 1, 'i': 2, 't': 1}),
    ({'g': 1, 'q': 1, 'a': 1, 'p': 1, 'd': 1, 't': 1, 'r': 2, 'e': 1}, 'pear', {'d': 1, 'p': 0, 'a': 0, 'q': 1, 'e': 0, 'g': 1, 'r': 1, 't': 1}),
    ({'d': 1, 'q': 1, 'o': 1, 'k': 2, 'c': 1, 'r': 2, 'u': 1}, 'duck', {'d': 0, 'c': 0, 'u': 0, 'k': 1, 'r': 2, 'q': 1, 'o': 1}),
    ({'l': 1, 'k': 1, 'm': 1, 'd': 1, 's': 1, 'i': 1, 'c': 1, 'e': 2}, 'milk', {'d': 1, 'c': 1, 'k': 0, 'e': 2, 'l': 0, 'm': 0, 's': 1, 'i': 0}),
    ({'b': 1, 'd': 1, 'q': 1, 'k': 1, 't': 1, 'i': 1, 'a': 1, 'e': 1}, 'tea', {'d': 1, 'k': 1, 'a': 0, 'q': 1, 'e': 0, 'b': 1, 'i': 1, 't': 0}),
])

def test_updateHand(hand, word, expected):
    actual = updateHand(hand, word)
    assert actual == expected

#--------------------------------------
# test bench for isValidWord
#--------------------------------------

@pytest.fixture
def read_wordList():
    return loadWords()

@pytest.mark.parametrize('word, hand, expected', [
    ('rapture', {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}, False),
    ('honey', {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}, True),
    ('honey', {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}, False),
    ('evil', {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}, True),
    ('even', {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}, False),
    ('kwijibo', {'b': 1, 'j': 1, 'k': 1, 'w': 1, 'o': 1, 'i': 2}, False),
    ('chayote', {'h': 1, 'u': 2, 'c': 2, 'a': 1, 'o': 2, 'y': 1, 'z': 1, 't': 2}, False),
    ('hammer', {'h': 1, 'm': 2, 'e': 1, 'a': 1, 'r': 1}, True),
    ('shrimp', {'h': 1, 's': 1, 'm': 1, 'b': 1, 'p': 1, 'u': 1, 'w': 1, 'r': 1, 'v': 1, 'i': 1}, True),
    ('chayote', {'h': 1, 's': 1, 'c': 1, 'g': 1, 'a': 1, 'q': 1, 'w': 1, 'o': 1, 'y': 1, 'e': 1, 't': 1}, True),
    ('duck', {'s': 1, 'u': 1, 'c': 1, 'k': 1, 'd': 1, 'y': 1, 'x': 1, 'n': 1}, True),
    ('teeth', {'h': 1, 'm': 1, 'k': 1, 'w': 1, 'e': 2, 'b': 1, 't': 2}, True),
    ('hair', {'n': 1, 'x': 1, 'w': 2, 'o': 2, 'y': 1, 'f': 3, 'p': 1, 't': 1}, False),
])

def test_isValidWord(read_wordList, word, hand, expected):
    actual = isValidWord(word, hand, read_wordList)
    assert actual == expected
    
#--------------------------------------
# test bench for calculateHandlen
#--------------------------------------

@pytest.mark.parametrize('hand, expected', [
    ({'b': 1, 'a': 1}, 2),
    ({'b': 1, 'c': 0, 'a': 1}, 2),
    ({}, 0),
    ({'z': 0, 'y': 0, 'x': 0}, 0),
    ({'z': 1, 'c': 1, 'r': 1, 'u': 1, 'a': 1, 'v': 2, 'k': 1, 'n': 1, 'x': 2, 'e': 1}, 12),
    ({'d': 1, 'p': 1, 'b': 2, 'l': 2, 'k': 1, 'n': 1, 'o': 2, 'e': 1, 'a': 1, 'f': 1, 'w': 1, 'y': 1, 'x': 1}, 16),
    ({'m': 1, 'z': 1, 'p': 1, 'a': 1, 'f': 1, 'i': 2, 'j': 1, 't': 2, 'x': 1}, 11),
])

def test_calculateHandlen(hand, expected):
    actual = calculateHandlen(hand)
    assert actual == expected
