# mortgage.py
#
# Exercise 1.7

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

while principal > 0:
    principal = principal - (payment-principal*rate/12)
    total_paid +=payment
    month +=1

print(f'Totally paid: {total_paid:0.2f} in {month} months')
