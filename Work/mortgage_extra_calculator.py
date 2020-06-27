# mortgage.py
#
# Exercise 1.9: Making an Extra Payment Calculator
# Modify the program so that extra payment information can be more generally handled. 
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/03_Numbers.md#exercise-110-making-a-table


# Exercise 1.10: Making a table
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/03_Numbers.md#exercise-110-making-a-table


# Exercise 1.11: Bonus
# While you’re at it, fix the program to correct for the overpayment that occurs in the last month.
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/03_Numbers.md#exercise-111-bonus

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

# Dave pays an extra $1000/month for 4 years starting in year 5 of the mortgage
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment= 1000.


while principal > 0:
    month +=1
    if month >= extra_payment_start_month and month <=extra_payment_end_month:
        extra = extra_payment
    else:
        extra = 0.
    principal = principal - (payment-principal*rate/12.) - extra
    if principal >=0:
        total_paid += payment + extra
    else:
        total_paid += principal + payment +extra
        principal = 0
    print('Month:', month, 'Paid:', round(total_paid,2), 'Principal:', round(principal,2))

print('Total paid:', round(total_paid, 2), 'Total months:', month)


