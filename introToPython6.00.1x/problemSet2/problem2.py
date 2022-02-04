###
#-------------------------------------------------------------------------------
# problem2.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2022
# Execution:    python3 problem2.py
#
# This program determines the fixed monthly payment needed to pay off a debt.
#
##

def fixedPayoff(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    initialBalance = balance
    fixedMonthlyPayment = 0
    while balance >= 0.0:
        balance = initialBalance
        fixedMonthlyPayment += 10
        for month in range(1, 13):
            monthlyUnpaidBalance = balance - fixedMonthlyPayment
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return f'Lowest payment: {fixedMonthlyPayment}'
