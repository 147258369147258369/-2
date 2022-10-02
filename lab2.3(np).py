import numpy as np
import timeit
arr = np.array([])
print('Введите элементы матрицы (3x3):')
for i in range(9):
    n = int(input())
    arr = np.append(arr, n)
arr.shape = (3, 3)
temp = np.linalg.matrix_power(arr, -1)
print(temp)
print(timeit.timeit())
