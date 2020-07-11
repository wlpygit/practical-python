# ticker.py
# Exercise 6.10: Making more pipeline components
# https://github.com/wlpygit/practical-python/blob/master/Notes/06_Generators/03_Producers_consumers.md#exercise-610-making-more-pipeline-components

from fileparse import parse_csv
from follow import follow
import csv
import report
import stock
import tableformat
from tableformat import print_table

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    # for row in rows:
    return (dict(zip(headers, row)) for row in rows)

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def filter_symbols(rows, names):
    # for row in rows:
    #     if row['name'] in names:
    yield (row for row in rows if row['name'] in names) 

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    
    formatter = tableformat.create_formatter(fmt)    
    formatter.headings(['Name','Price','Change'])

    # Read portfolio data file
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] for row in rows)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)