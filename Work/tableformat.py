# tableformat.py

# Exercise 4.5: An Extensibility Problem
# https://github.com/wlpygit/practical-python/blob/master/Notes/04_Classes_objects/02_Inheritance.md#exercise-45-an-extensibility-problem
# 
# Exercise 4.11: Defining a custom exception
# https://github.com/wlpygit/practical-python/blob/master/Notes/04_Classes_objects/04_Defining_exceptions.md#exercise-411-defining-a-custom-exception

def create_formatter(fmt):
    '''
    Create formatter
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')

def print_table(portfolio, columns: list, formatter):
    '''
    Create a table print selected columns
    '''
    formatter.headings(columns)
    for s in portfolio:
        rowdata = [str(getattr(s, colname)) for colname in columns]
        formatter.row(rowdata)
    return


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit a table in plain-text format
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print(f'{d:>10s}', end= ' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        h_html =''
        for h in headers:
            h_html += '<th>'+str(h)+'</th>'
        print('<tr>'+h_html+'</tr>')

    def row(self, rowdata):
        s_html =''
        for s in rowdata:
            s_html +='<td>'+str(s)+'</td>'
        print('<tr>'+s_html+'</tr>')

class FormatError(Exception):
    def __repr__(self):
        return self
    