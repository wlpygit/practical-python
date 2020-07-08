# fileparse.py
#
# Exercise 3.3
# https://github.com/wlpygit/practical-python/blob/master/Notes/03_Program_organization/02_More_functions.md#exercise-33-reading-csv-files

# Exercise 3.17: From filenames to file-like objects
# https://github.com/wlpygit/practical-python/blob/master/Notes/03_Program_organization/06_Design_discussion.md#exercise-317-from-filenames-to-file-like-objects


import csv

def parse_csv(filename, select=None, types=[str, int, float], delimiter=',', has_headers = True):
    """
    Parse a CSV file into a list of records 
    """
    records = []    
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            for row in rows:
                if not row:     # Skip rows with no data
                    continue
                # row =[func(val) for func, val in list(zip(types, row))]
                try:
                    record = dict(zip(headers, list(func(val) for func, val in list(zip(types, row)))))
                except ValueError as e:
                    print('Couldn\'t convert', row)
                    print('Reason', e)
                if select and types:
                    # d ={}
                    # # for i in select:
                    #     d[i] = record[i]
                    # r = [record[i] for i in select]
                    record = dict(zip(select, [record[i] for i in select]))
                records.append(record)
        else:
            for row in rows:
                if not row:     # Skip rows with no data
                    continue
                # record=(row[0], float(row[1]))
                record= list(func(val) for func, val in list(zip(types, row)))
                records.append(record)

    return records

# print(parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int]))
# print(parse_csv('Data/portfolio.csv', select=['name'], types=[str]))

# print(parse_csv('Data/portfolio.csv'))
# print(parse_csv('Data/portfolio.dat', select=['name', 'shares'], types=[str, int], delimiter=' '))
# print(parse_csv('Data/prices.csv', select=['name','price'],types=[str, float], has_headers=False))
# print(parse_csv('Data/prices.csv', types=[str, float], has_headers=False))