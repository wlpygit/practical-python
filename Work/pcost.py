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

# Exercise 3.14: Using more library imports
# https://github.com/wlpygit/practical-python/blob/master/Notes/03_Program_organization/04_Modules.md#exercise-314-using-more-library-imports
# Modify the pcost.py file so that it uses the report.read_portfolio() function.

import csv
import sys
import fileparse

def portfolio_cost(filename):
    """     
    f = open(filename)
    rows = csv.reader(f)
    headers=next(rows)

    cost = 0

    for i, row in enumerate(rows):
        record = dict(zip(headers, row))
        # row = line.split(',')
        try:
            shares = int(record['shares'])
            price = float(record['price'])
            cost += shares*price
        except ValueError:
            print(f'Row {i}: Bad row {row}')
    """
    portfolio = fileparse.parse_csv(filename, select=['name','shares','price'],types=[str, int, float])
    # print(portfolio)
    cost = 0
    for r in portfolio:
        cost += r['shares']*r['price']

    return cost

# Main function
def main(argv):
    # Parse command line args, environment, etc.
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost is: ${cost:0.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)

