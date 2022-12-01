import statistics

def total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def mean(numbers):
    mean = statistics.mean(numbers)
    return mean

def median(numbers):
    median = statistics.median(numbers)
    return median

# ...

# Path: simplestats.py
# Compare this snippet from github.py:
# """String tools.
#
# This module contains various string tools.
#
# Authors:
#     Philipp Buling <