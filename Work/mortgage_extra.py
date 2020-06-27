# mortgage.py
#
# Exercise 1.8: Extra payments
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/03_Numbers.md

""" Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s
 Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and 
the monthly payment is $2684.11.

Here is a program that calculates the total amount that Dave will have to pay over the 
life of the mortgage: """

principal = 500000.
rate = .05
payment = 2684.11
total_paid = 0.0
month = 0


extra_payment= 1000.


while principal > 0:
    month +=1
    if month <= 12:             # extra payment of $1000.0 for first 12 months
        extra = extra_payment
    else:
        extra = 0.
    principal = principal - (payment-principal*rate/12) - extra
    total_paid +=payment+extra

print('Total paid:', round(total_paid, 2), 'Total months:', month)


