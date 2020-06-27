# pcost.py
#
# Exercise 1.27
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/06_Files.md#exercise-127-reading-a-data-file

# Exercise 1.30
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/07_Functions.md#exercise-130-turning-a-script-into-a-function
""" Take the code you wrote for the pcost.py program in Exercise 1.27 and turn it into a 
    function portfolio_cost(filename). This function takes a filename as input, reads the 
    portfolio data in that file, and returns the total cost of the portfolio as a float. """

# Exercise 1.32: Using a library function

# Exercise 1.33: Reading from the command line
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/07_Functions.md#exercise-133-reading-from-the-command-line


import csv
import sys

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    cost = 0

    for row in rows:
        # row = line.split(',')
        try:
            shares = int(row[1])
        except ValueError:
            print("Couldn't parse", row)
        cost += shares*float(row[2])
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
# cost = portfolio_cost('Data/missing.csv')
print(f'Total cost is: ${cost:0.2f}')


