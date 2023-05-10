def sort(a, size):
    vergleiche = 0
    vertauschungen = 0
    for stack in range(size):
        vertauscht = False
        for i in range(size - stack - 1):
            vergleiche += 1
            if a[i] > a[i + 1]:
                vertauschungen += 1
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                vertauscht = True
        if not vertauscht:
            break
    print(vergleiche, vertauschungen)
    return a


print(sort([61, 42, 59, 14, 23, 79, 37, 92], len([61, 42, 59, 14, 23, 79, 37, 92])))
print(sort([14, 23, 37, 42, 59, 61, 79, 92], len([14, 23, 37, 42, 59, 61, 79, 92])))
print(sort(sorted([14, 23, 37, 42, 59, 61, 79, 92], reverse=True), len([14, 23, 37, 42, 59, 61, 79, 92])))
