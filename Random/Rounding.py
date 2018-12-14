# Given a list of decimals and integer target sum
# Find a way to ceil/floor each value such that:
#   - all values become integers that add up to the sum exactly
#   - the cumulative absolute diff between the integers and their decimal forms are minimal

# Greedy:
# First assume each number is rounded down
# Obtain the diff remaining (this should be a positive value less than or equal to length of the list)
# Sort the list by the decimal component of each number (Descending)
# Add 1 to the first 'diff' number of elements (round up the numbers with the largest decimal parts enough to get to the target)
#   - Since these numbers have the biggest decimal component, rounding them up will minimize the cumulative absolute difference
# Retain the original indices and return in order

import math

def prices(pr, tr):
    data = list(zip([math.floor(p) for p in pr], [p % 1 for p in pr], range(len(pr))))
    data.sort(key = lambda x:x[1], reverse=True)
    data = [[d[0], d[2]] for d in data]
    diff = tr - sum(d[0] for d in data)
    if diff < 0 or diff > len(pr):
        return False
    for i in range(diff):
        data[i][0] += 1
    data.sort(key = lambda x:x[1])
    return [d[0] for d in data]

print(prices([1.1, 1.2, 1.7], 5))
print(prices([1.1, 1.2, 1.7], 7))
print(prices([1.2, 1.1, 1.7, 1.2], 7))
print(prices([1.5, 1.3, 1.5, 1.2], 7))
print(prices([1.1, 1.2, 1.7], 3))