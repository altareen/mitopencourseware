###
#-------------------------------------------------------------------------------
# problem1.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2022
# Execution:    python3 problem1.py
#
# This program determines the credit card balance after 1 year of payments.
#
##

def minimumPayments(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    for month in range(1, 13):
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return f'Remaining balance: {round(balance, 2)}'
