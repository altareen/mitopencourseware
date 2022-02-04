###
#-------------------------------------------------------------------------------
# test_problem2.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the problem2.py code.
#
##

from problem2 import fixedPayoff
import pytest

@pytest.mark.parametrize('balance, annualInterestRate, expected', [
    (3329, 0.2, 'Lowest payment: 310'),
    (4773, 0.2, 'Lowest payment: 440'),
    (3926, 0.2, 'Lowest payment: 360'),
    (103, 0.2, 'Lowest payment: 10'),
    (814, 0.2, 'Lowest payment: 80'),
    (528, 0.2, 'Lowest payment: 50'),
    (97, 0.2, 'Lowest payment: 10'),
    (4127, 0.18, 'Lowest payment: 380'),
    (4675, 0.15, 'Lowest payment: 420'),
    (4453, 0.04, 'Lowest payment: 380'),
    (3075, 0.2, 'Lowest payment: 290'),
    (3872, 0.15, 'Lowest payment: 350'),
    (3696, 0.2, 'Lowest payment: 340'),
    (4185, 0.2, 'Lowest payment: 390'),
    (3897, 0.04, 'Lowest payment: 340'),
])

def test_result(balance, annualInterestRate, expected):
    actual = fixedPayoff(balance, annualInterestRate)
    assert actual == expected
