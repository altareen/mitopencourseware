###
#-------------------------------------------------------------------------------
# test_problem1.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the problem1.py code.
#
##

from problem1 import minimumPayments
import pytest

@pytest.mark.parametrize('balance, annualInterestRate, monthlyPaymentRate, expected', [
    (42, 0.2, 0.04, 'Remaining balance: 31.38'),
    (484, 0.2, 0.04, 'Remaining balance: 361.61'),
    (325, 0.15, 0.08, 'Remaining balance: 138.7'),
    (488, 0.15, 0.06, 'Remaining balance: 269.58'),
    (68, 0.15, 0.08, 'Remaining balance: 29.02'),
    (187, 0.18, 0.04, 'Remaining balance: 136.99'),
])

def test_result(balance, annualInterestRate, monthlyPaymentRate, expected):
    actual = minimumPayments(balance, annualInterestRate, monthlyPaymentRate)
    assert actual == expected
