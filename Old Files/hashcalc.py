def single_digit_sum(zahl):
    ziffern = [int(ziffer) for ziffer in str(zahl)]
    return sum(ziffern) if len(ziffern) == 1 else single_digit_sum(sum(ziffern))


print(single_digit_sum(12345684))
modulo = 12345684 % 9
print(modulo)
