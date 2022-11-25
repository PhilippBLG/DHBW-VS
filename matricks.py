import neighborhood

print("====== Largest Neighbors =====")
while True:
    height = input("Height: ")
    width = input("width: ")
    if not height.isdecimal() or not width.isdecimal():
        break
    matrix = neighborhood.create_matrix(int(height), int(width))
    print('\n'.join('\t'.join(str(number) for number in row) for row in matrix))
    print("Largest neighbors: ")
    print(neighborhood.find_largest_neighbors(matrix))

print("Thanks for using our Neighbor finder")