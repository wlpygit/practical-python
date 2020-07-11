# follow.py
# Exercise 6.5: Monitoring a streaming data source
# https://github.com/wlpygit/practical-python/blob/master/Notes/06_Generators/02_Customizing_iteration.md#exercise-65-monitoring-a-streaming-data-source

import os
import time
import report

def follow(file):
    f = open(file)
    f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line =='':
            time.sleep(0.1)
            continue
        yield line

# Exercise 6.8: Setting up a simple pipeline
# https://github.com/wlpygit/practical-python/blob/master/Notes/06_Generators/03_Producers_consumers.md#exercise-68-setting-up-a-simple-pipeline

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

if __name__ =='__main__':
    for line in follow('Data/stocklog.csv'):
        # line = f.readline()
        # if line =='':
        #     time.sleep(0.1)     # Sleep briefly and retry
        #     continue
        portfolio = report.read_portfolio('Data/portfolio.csv')

        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:10.2f} {change:>10.2f}')

