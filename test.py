def total(low, high):

    if low == high:
        return low

    return high + total(low, high - 1)


print(total(1,10))