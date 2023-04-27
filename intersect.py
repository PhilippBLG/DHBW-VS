def intersect(a, b):
    intersection = []
    for element in a:
        if element in b:
            intersection.append(element)
    return intersection

print(intersect([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))