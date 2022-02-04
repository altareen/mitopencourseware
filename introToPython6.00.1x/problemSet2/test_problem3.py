###
#-------------------------------------------------------------------------------
# test_problem3.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2022
# Execution:    pytest -v
#
# This program is the pytest test bench for the problem3.py code.
#
##

from problem3 import bisectionPayoff
import pytest

@pytest.mark.parametrize('balance, annualInterestRate, expected', [
    (320000, 0.2, 'Lowest payment: 29157.09'),
    (999999, 0.18, 'Lowest payment: 90325.03'),
    (287546, 0.2, 'Lowest payment: 26200.01'),
    (103064, 0.18, 'Lowest payment: 9309.27'),
    (485178, 0.22, 'Lowest payment: 44592.41'),
    (303721, 0.22, 'Lowest payment: 27914.81'),
    (307054, 0.22, 'Lowest payment: 28221.14'),
    (41176, 0.15, 'Lowest payment: 3670.59'),
    (324246, 0.15, 'Lowest payment: 28904.59'),
    (90139, 0.2, 'Lowest payment: 8213.1'),
    (31901, 0.2, 'Lowest payment: 2906.69'),
    (126284, 0.21, 'Lowest payment: 11556.54'),
])

def test_result(balance, annualInterestRate, expected):
    actual = bisectionPayoff(balance, annualInterestRate)
    assert actual == expected
