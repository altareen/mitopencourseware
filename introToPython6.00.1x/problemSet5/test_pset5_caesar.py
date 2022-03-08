###
#-------------------------------------------------------------------------------
# test_pset5_caesar.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Mar 07, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the pset5_caesar.py code.
#
##

from pset5_caesar import *
import pytest

#--------------------------------------
# test bench for Message.build_shift_dict
#--------------------------------------

@pytest.mark.parametrize('shift, expected', [
    (0, {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}),
    (2, {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'}),
    (16, {'a': 'q', 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f': 'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z', 'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 't': 'j', 'u': 'k', 'v': 'l', 'w': 'm', 'x': 'n', 'y': 'o', 'z': 'p', 'A': 'Q', 'B': 'R', 'C': 'S', 'D': 'T', 'E': 'U', 'F': 'V', 'G': 'W', 'H': 'X', 'I': 'Y', 'J': 'Z', 'K': 'A', 'L': 'B', 'M': 'C', 'N': 'D', 'O': 'E', 'P': 'F', 'Q': 'G', 'R': 'H', 'S': 'I', 'T': 'J', 'U': 'K', 'V': 'L', 'W': 'M', 'X': 'N', 'Y': 'O', 'Z': 'P'}),
    (25, {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y', 'A': 'Z', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E', 'G': 'F', 'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q', 'S': 'R', 'T': 'S', 'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y'}),
])

def test_build_shift_dict(shift, expected):
    message = Message('hello')
    actual = message.build_shift_dict(shift)
    assert actual == expected

#--------------------------------------
# test bench for Message.apply_shift
#--------------------------------------

@pytest.mark.parametrize('shift, text, expected', [
    (0, 'hello', 'hello'),
    (6, 'we are taking 6.00.1x', 'ck gxk zgqotm 6.00.1d'),
    (13, 'th!s is Problem Set 6?', 'gu!f vf Ceboyrz Frg 6?'),
    (7, 'TESTING.... so many words we are testing out your code: last one', 'ALZAPUN.... zv thuf dvykz dl hyl alzapun vba fvby jvkl: shza vul'),
])

def test_apply_shift(shift, text, expected):
    message = Message(text)
    actual = message.apply_shift(shift)
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.get_shift
#--------------------------------------

@pytest.mark.parametrize('text, shift, expected', [
    ('1.hello!!', 7, 7),
])

def test_get_shift(text, shift, expected):
    plaintext = PlaintextMessage(text, shift)
    actual = plaintext.get_shift()
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.get_encrypting_dict
#--------------------------------------

@pytest.mark.parametrize('text, shift, expected', [
    ('1.hello!!', 9, {'a': 'j', 'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 'j': 's', 'k': 't', 'l': 'u', 'm': 'v', 'n': 'w', 'o': 'x', 'p': 'y', 'q': 'z', 'r': 'a', 's': 'b', 't': 'c', 'u': 'd', 'v': 'e', 'w': 'f', 'x': 'g', 'y': 'h', 'z': 'i', 'A': 'J', 'B': 'K', 'C': 'L', 'D': 'M', 'E': 'N', 'F': 'O', 'G': 'P', 'H': 'Q', 'I': 'R', 'J': 'S', 'K': 'T', 'L': 'U', 'M': 'V', 'N': 'W', 'O': 'X', 'P': 'Y', 'Q': 'Z', 'R': 'A', 'S': 'B', 'T': 'C', 'U': 'D', 'V': 'E', 'W': 'F', 'X': 'G', 'Y': 'H', 'Z': 'I'}),
])

def test_get_encrypting_dict(text, shift, expected):
    plaintext = PlaintextMessage(text, shift)
    actual = plaintext.get_encrypting_dict()
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.get_message_text_encrypted
#--------------------------------------

@pytest.mark.parametrize('text, shift, expected', [
    ('1.hello!!', 2, '1.jgnnq!!'),
])

def test_get_message_text_encrypted(text, shift, expected):
    plaintext = PlaintextMessage(text, shift)
    actual = plaintext.get_message_text_encrypted()
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.change_shift
#--------------------------------------

@pytest.mark.parametrize('text, shift, updated_shift, expected', [
    ('1.hello!!', 4, 18, 18),
])

def test_change_shift(text, shift, updated_shift, expected):
    plaintext = PlaintextMessage(text, shift)
    plaintext.change_shift(updated_shift)
    actual = plaintext.get_shift()
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.change_shift
#--------------------------------------

@pytest.mark.parametrize('text, shift, updated_shift, expected', [
    ('1.hello!!', 5, 15, {'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u', 'g': 'v', 'h': 'w', 'i': 'x', 'j': 'y', 'k': 'z', 'l': 'a', 'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e', 'q': 'f', 'r': 'g', 's': 'h', 't': 'i', 'u': 'j', 'v': 'k', 'w': 'l', 'x': 'm', 'y': 'n', 'z': 'o', 'A': 'P', 'B': 'Q', 'C': 'R', 'D': 'S', 'E': 'T', 'F': 'U', 'G': 'V', 'H': 'W', 'I': 'X', 'J': 'Y', 'K': 'Z', 'L': 'A', 'M': 'B', 'N': 'C', 'O': 'D', 'P': 'E', 'Q': 'F', 'R': 'G', 'S': 'H', 'T': 'I', 'U': 'J', 'V': 'K', 'W': 'L', 'X': 'M', 'Y': 'N', 'Z': 'O'}),
])

def test_change_shift(text, shift, updated_shift, expected):
    plaintext = PlaintextMessage(text, shift)
    plaintext.change_shift(updated_shift)
    actual = plaintext.get_encrypting_dict()
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.change_shift
#--------------------------------------

@pytest.mark.parametrize('text, shift, updated_shift, expected', [
    ('1.hello!!', 6, 21, '1.czggj!!'),
])

def test_change_shift(text, shift, updated_shift, expected):
    plaintext = PlaintextMessage(text, shift)
    plaintext.change_shift(updated_shift)
    actual = plaintext.get_message_text_encrypted()
    assert actual == expected

#--------------------------------------
# test bench for PlaintextMessage.change_shift
#--------------------------------------

@pytest.mark.parametrize('text, shift, updated_shift, expected', [
    ('1.hello!!', 7, 24, None),
])

def test_change_shift(text, shift, updated_shift, expected):
    plaintext = PlaintextMessage(text, shift)
    actual = plaintext.change_shift(updated_shift)
    assert actual == expected

#--------------------------------------
# test bench for CiphertextMessage.decrypt_message
#--------------------------------------

@pytest.mark.parametrize('text, expected', [
    (get_story_string(), (16, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.')),
])

def test_decrypt_message(text, expected):
    ciphertext = CiphertextMessage(text)
    actual = ciphertext.decrypt_message()
    assert actual == expected
