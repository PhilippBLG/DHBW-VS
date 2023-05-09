"""String tools.

This module returns us the mean and median of a list of numbers.

Authors:
    Philipp Buling <philipp.buling@icloud.com>


.. _`Python Standard Library`:
    https://docs.python.org/3.11/library

"""

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
