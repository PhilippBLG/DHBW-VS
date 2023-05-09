def find_ducpliates(array):
    doubles = {}
    for letter in array:
        if doubles.get(letter):
            return letter
        doubles[letter] = True
    return None

def missing_alphabet(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in string:
            return letter
    return None

def first_nondouble(string):
    for letter in string:
        if string.count(letter) == 1:
            return letter
    return None


print(find_ducpliates(["a", "b", "c", "d", "c", "e", "f"]))
print(missing_alphabet("the quick brown box jumps over a lazy dog"))
print(first_nondouble("minimum"))


