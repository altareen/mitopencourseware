###
#-------------------------------------------------------------------------------
# problem3.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2022
# Execution:    python3 problem3.py
#
# This program determines the fixed monthly payment needed to pay off a debt.
#
##

def bisectionPayoff(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    initialBalance = balance
    lowerBound = balance / 12.0
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    fixedMonthlyPayment = 0

    while not (0.0 <= balance <= 0.01):
        balance = initialBalance
        fixedMonthlyPayment = (lowerBound + upperBound) / 2.0
        for month in range(1, 13):
            monthlyUnpaidBalance = balance - fixedMonthlyPayment
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if balance < 0.0:
            upperBound = fixedMonthlyPayment
        else:
            lowerBound = fixedMonthlyPayment
    return f'Lowest payment: {round(fixedMonthlyPayment, 2)}'
