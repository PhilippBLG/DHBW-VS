def intersect(a, b):
    intersection = []
    for element in a:
        if element in b:
            intersection.append(element)
    return intersection