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
import stock
import report

def portfolio_cost(file):
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
    # Quote it out after building a portfolio class in Exercise 6.2
    """     
    portdicts = fileparse.parse_csv(file, select=['name','shares','price'],types=[str, int, float])
    # print(portfolio)
    cost = 0
    portfolio = [stock.Stock(d['name'],d['shares'],d['price']) for d in portdicts]
    for s in portfolio:
        cost += s.shares*s.price 
    """
    
    portfolio = report.read_portfolio(file)

    return portfolio.total_cost

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

