def find_ducpliates(array):
    doubles = {}
    for letter in array:
        if doubles.get(letter):
            return letter
        doubles[letter] = True
    return None



def missing_alphabet(string):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in string:
            return letter
    return None


def first_nondouble(string):
    doubles = {}
    for letter in string:
        doubles[letter] = doubles.get(letter, 0) + 1
    for letter in doubles:
        if doubles.get(letter) == 1:
            return letter


print(find_ducpliates(["a", "b", "c", "d", "c", "e", "f"]))
print(missing_alphabet("the quick brown box jumps over a lazy dog"))
print(first_nondouble("minimum"))
