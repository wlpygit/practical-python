# report.py
#
# Exercise 2.4

# Exercise 2.4: A list of tuples

# Exercise 2.5: List of Dictionaries
# https://github.com/wlpygit/practical-python/blob/master/Notes/02_Working_with_data/02_Containers.md#exercise-25-list-of-dictionaries
""" Take the function you wrote in Exercise 2.4 and modify to represent 
each stock in the portfolio with a dictionary instead of a tuple. In 
this dictionary use the field names of "name", "shares", and "price" to 
represent the different columns in the input file. """

# Exercise 2.7: Finding out if you can retire

# Exercise 3.12: Using your library module
# https://github.com/wlpygit/practical-python/blob/master/Notes/03_Program_organization/04_Modules.md#exercise-312-using-your-library-module

# Exercise 3.15: main() functions
# add a main() function that accepts a list of command line options and produces the same output as before. 

import csv
from fileparse import parse_csv

def read_portfolio(filename):
    """     
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # holding = {
            #     headers[0]: row[0], 
            #     headers[1]: int(row[1]),
            #     headers[2]: float(row[2])
            # }
            holding = dict(zip(headers, row))
            holding[headers[1]]=int(holding[headers[1]])
            holding[headers[2]]=float(holding[headers[2]])
            portfolio.append(holding)  
    """
    portfolio = parse_csv(filename, select=None, types=[str, int, float], delimiter=',')
    return portfolio

def read_prices(filename):
    """     
    prices={}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # print(row)
            if len(row) != 0:
                prices[row[0]]=float(row[1]) 
    """
    pricelist = parse_csv(filename, types=[str, float], has_headers=False)
    return pricelist

def make_report(portofolio, pricelist):
    """ 
    generate report from portfolio and prices
    return report as a list of tuples
    """
    
    report = []
    prices = dict(pricelist)
    for item in portofolio:
        name = item['name']
        shares = item['shares']
        price = prices[item['name']]
        change = price - item['price']
        report.append((name, shares, price, change))
    
    return report       # list of tuples 

def print_report(report: list):
    """ 
    print report from report (list of tuple) with headers info
    """
    cost = 0
    current = 0

    print('... look at the output ...')  
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 +' ')*len(headers))

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')
        cost += shares*(price-change)
        current += shares*price
    # for r in report:
    #     print('%10s %10d %10.2f %10.2f' % r)
    
    print(f'Total cost of portfolio is: ${cost:0.2f}')
    print(f'Current portfolio value is: ${current:0.2f}')

    if cost < current:
        print(f'You earned: ${current-cost:0.2f}')
    elif cost > current:
        print(f'You lose: ${cost-current:0.2f}')
    else:
        print('You are even.')

    return
        
# if __name__ == "__main__":
def portfolio_report(portfolio_filename, prices_filename):
    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

    return

# portfolio_report('Data/portfolio.csv','Data/prices.csv')

# Main function
def main(argv):
    # Parse command line args, environment, etc.
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)

if __name__ == '__main__':
    import sys
    main(sys.argv)

        
