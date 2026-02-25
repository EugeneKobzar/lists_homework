my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(my_matrix)
# for 90° rotation
for i in range(n // 2):
    for j in range(i, n -1 - i):
        temp = my_matrix[i][j]
        my_matrix[i][j] = my_matrix[n - 1 - j][i]
        my_matrix[n - 1 - j][i] = my_matrix[n - 1 - i][n - 1 - j]
        my_matrix[n - 1 - i][n - 1 - j] = my_matrix[j][n - 1 - i]
        my_matrix[j][n - 1 - i] = temp
print('90° rotation:')
for row in my_matrix:
    print(row)
    # for 180° rotation
for i in range(n // 2):
    for j in range(i, n -1 - i):
        temp = my_matrix[i][j]
        my_matrix[i][j] = my_matrix[n - 1 - j][i]
        my_matrix[n - 1 - j][i] = my_matrix[n - 1 - i][n - 1 - j]
        my_matrix[n - 1 - i][n - 1 - j] = my_matrix[j][n - 1 - i]
        my_matrix[j][n - 1 - i] = temp
print('180° rotation:')
for row in my_matrix:
    print(row)
    # for 270° rotation
for i in range(n // 2):
    for j in range(i, n - 1 - i):
        temp = my_matrix[i][j]
        my_matrix[i][j] = my_matrix[n - 1 - j][i]
        my_matrix[n - 1 - j][i] = my_matrix[n - 1 - i][n - 1 - j]
        my_matrix[n - 1 - i][n - 1 - j] = my_matrix[j][n - 1 - i]
        my_matrix[j][n - 1 - i] = temp
print('270° rotation:')
for row in my_matrix:
    print(row)

