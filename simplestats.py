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
