import random

def mx_ini(row, column):
    arr = []
    for i in range(row):
        a = []
        for j in range(column):
            a.append(random.randint(-99, 99))
        arr.append(a)
    return arr

def mx_out(arr, num):
    print(f"Массив {num}")
    for i in arr:
        print(i)

row = int(input())
column = int(input())
matrix_1 = mx_ini(row, column)
matrix_2 = mx_ini(row, column)
mx_out(matrix_1, 1)
mx_out(matrix_2, 2)
matrix_3 = [[0] * column for i in range(row)]
for i in range(row):
    for j in range(column):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
mx_out(matrix_3, 3)
