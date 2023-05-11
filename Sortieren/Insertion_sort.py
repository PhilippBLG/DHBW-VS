def sort(a, size):
    vergleiche = 0
    vertauschungen = 0
    for i in range(1, size):
        temp = a[i-1]
        j = i
        while a[j] < a[j-1] and j > 0:
            vergleiche += 1
            vertauschungen += 1
            a[j-1] = a[j]
            a[j] = temp
            j -= 1
            temp = a[j-1]
        vergleiche += 1
    return vergleiche, vertauschungen, a


print(sort([61, 42, 59, 14, 23, 79, 37, 92], len([61, 42, 59, 14, 23, 79, 37, 92])))
print(sort([4, 2, 7, 1, 3], len([4, 2, 7, 1, 3])))
