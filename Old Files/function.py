def solid(a, b=0, c=1, cube=False):
    if cube:
        return a ** 3
    return a * b * c


print(solid(3, 4))  # 12 (rectangle area)
print(solid(3, 4, 1))  # 12 (volume of cuboid)
print(solid(3, 4, 5))  # 60 (volume of cuboid)
print(solid(3, cube=True))  # 27 (volume of cube)
print(solid(3))  # 0  (line has no volume or area)
