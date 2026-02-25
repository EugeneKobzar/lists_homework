my_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for row in my_matrix:
    print(row)
total = 0
for row in my_matrix:
    for number in row:
        total += number
print('Total amount', total)