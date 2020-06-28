# collection_fun.py
#
# 2.5 collections module
# https://github.com/wlpygit/practical-python/blob/master/Notes/02_Working_with_data/05_Collections.md#25-collections-module

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# Counting Things - Counters
from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares
print(total_shares)

# One-Many Mappings -defaultdict
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
print(holdings)

# Keeping a History - deque

""" 
from collections import deque
history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line) 
"""
