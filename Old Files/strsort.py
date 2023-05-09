def strsort(x):
    return "".join(sorted(x))

sort = input("Bitte sortieren: ")
while sort:
    stringsorted = strsort(sort)
    print(stringsorted)
    sort = input("Bitte sortieren: ")

print("Danke fürs Sortieren")