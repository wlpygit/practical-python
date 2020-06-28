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

import csv

def read_portfolio(filename):
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
    return portfolio

def read_prices(filename):
    prices={}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # print(row)
            if len(row) != 0:
                prices[row[0]]=float(row[1])
    return prices

def make_report(portofolio, prices):
    
    report = []
    for item in portofolio:
        name = item['name']
        shares = item['shares']
        price = prices[item['name']]
        change = price - item['price']
        report.append((name, shares, price, change))
    
    return report       # list of tuples 
        
if __name__ == "__main__":
    
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    
    cost = 0
    current = 0
    item = {}

    for item in portfolio:
        cost += item['shares']*item['price']
        current += item['shares']*prices[item['name']]

    report = make_report(portfolio, prices)
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print((''*10 +' ')*4)

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')
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
        
