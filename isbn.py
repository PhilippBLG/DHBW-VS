def check(isbn):
    checksum = 0
    for x in liste[1:12:2]:
        checksum += int(x)*3
    for x in liste[0:12:2]:
        checksum += int(x)
    checknumber = 10 - int(str(checksum)[-1])
    if int(checknumber) == int(isbn[-1]):
        return True
    else:
        return False

isbn = input("Was ist die ISBN? ")
while isbn:
    liste = list(isbn.replace("-", ""))
    print(check(liste))
    isbn = input("Was ist die ISBN? ")

print("Danke fürs benutzen unseres Validators")