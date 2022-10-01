import numpy as np
arr = np.array([])
arr1 = np.array([])
arr = arr.astype(np.int64)
arr1 = arr1.astype(np.int64)
print('Выберите функцию:', 'Транспонирование матрицы', 'Умножение матриц', 'Определение ранга матрицы', sep='\n')
func = str(input())
if func == 'Транспонирование матрицы':
    num = input('Введите размер матрицы (1х2, 2х1, 1х3, 3х1, 2х2, 3х3): ')
    if num == '1x2':
        print('Введите элементы матрицы:')
        for i in range(2):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (1, 2)
        temp = arr.transpose()
        print(temp)
    elif num == '2x1':
        print('Введите элементы матрицы:')
        for i in range(2):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (2, 1)
        temp = arr.transpose()
        print(temp)
    elif num == '3x1':
        print('Введите элементы матрицы:')
        for i in range(3):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (3, 1)
        temp = arr.transpose()
        print(temp)
    elif num == '1x3':
        print('Введите элементы матрицы:')
        for i in range(3):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (1, 3)
        temp = arr.transpose()
        print(temp)
    elif num == '2x2':
        print('Введите элементы матрицы:')
        for i in range(4):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (2, 2)
        temp = arr.transpose()
        print(temp)
    elif num == '3x3':
        print('Введите элементы матрицы:')
        for i in range(9):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (3, 3)
        temp = arr.transpose()
        print(temp)
if func == 'Умножение матриц':
    num = input('Введите размер первой матрицы (1х2, 2х1, 1х3, 3х1, 2х2, 3х3): ')
    if num == '1x2':
        print('Введите элементы первой матрицы:')
        for i in range(2):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (1, 2)
        num1 = input('Введите размер второй матрицы (2х1, 2х2): ')
        if num1 == '2x1':
            print('Введите элементы второй матрицы:')
            for i in range(2):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (2, 1)
        elif num1 == '2x2':
            print('Введите элементы второй матрицы:')
            for i in range(4):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (2, 2)
        temp = arr.dot(arr1)
        print(temp)
    elif num == '2x1':
        print('Введите элементы первой матрицы:')
        for i in range(2):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (2, 1)
        num1 = input('Введите размер второй матрицы (1х2, 2х2): ')
        if num1 == '1x2':
            print('Введите элементы второй матрицы:')
            for i in range(2):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (1, 2)
        elif num1 == '2x2':
            print('Введите элементы второй матрицы:')
            for i in range(4):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (2, 2)
        temp = arr.dot(arr1)
        print(temp)
    elif num == '1x3':
        print('Введите элементы первой матрицы:')
        for i in range(3):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (1, 3)
        num1 = input('Введите размер второй матрицы (3х1, 3х3): ')
        if num1 == '3x1':
            print('Введите элементы второй матрицы:')
            for i in range(3):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (3, 1)
        elif num1 == '3x3':
            print('Введите элементы второй матрицы:')
            for i in range(9):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (3, 3)
        temp = arr.dot(arr1)
        print(temp)
    elif num == '3x1':
        print('Введите элементы первой матрицы:')
        for i in range(3):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (3, 1)
        num1 = input('Введите размер второй матрицы (1х3, 3х3): ')
        if num1 == '1x3':
            print('Введите элементы второй матрицы:')
            for i in range(3):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (1, 3)
        elif num1 == '3x3':
            print('Введите элементы второй матрицы:')
            for i in range(9):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (3, 3)
        temp = arr.dot(arr1)
        print(temp)
    elif num == '2x2':
        print('Введите элементы первой матрицы:')
        for i in range(4):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (2, 2)
        num1 = input('Введите размер второй матрицы (2х1, 2х2): ')
        if num1 == '2x1':
            print('Введите элементы второй матрицы:')
            for i in range(2):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (2, 1)
        elif num1 == '2x2':
            print('Введите элементы второй матрицы:')
            for i in range(4):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (2, 2)
        temp = arr.dot(arr1)
        print(temp)
    elif num == '3x3':
        print('Введите элементы первой матрицы:')
        for i in range(9):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (3, 3)
        num1 = input('Введите размер второй матрицы (3х1, 3х3): ')
        if num1 == '3x1':
            print('Введите элементы второй матрицы')
            for i in range(3):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (3, 1)
        elif num1 == '3x3':
            print('Введите элементы второй матрицы')
            for i in range(9):
                n = int(input())
                arr1 = np.append(arr1, n)
            arr1.shape = (3, 3)
        temp = arr.dot(arr1)
        print(temp)
if func == 'Определение ранга матрицы':
    num = input('Введите размер матрицы (1х2, 2х1, 1х3, 3х1, 2х2, 3х3): ')
    if num == '1x2':
        print('Введите элементы матрицы:')
        for i in range(2):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (1, 2)
        temp = np.linalg.matrix_rank(arr)
        print('Ранг матрицы', temp)
    elif num == '2x1':
        print('Введите элементы матрицы:')
        for i in range(2):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (2, 1)
        temp = np.linalg.matrix_rank(arr)
        print('Ранг матрицы', temp)
    elif num == '3x1':
        print('Введите элементы матрицы:')
        for i in range(3):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (3, 1)
        temp = np.linalg.matrix_rank(arr)
        print('Ранг матрицы', temp)
    elif num == '1x3':
        print('Введите элементы матрицы:')
        for i in range(3):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (1, 3)
        temp = np.linalg.matrix_rank(arr)
        print('Ранг матрицы', temp)
    elif num == '2x2':
        print('Введите элементы матрицы:')
        for i in range(4):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (2, 2)
        temp = np.linalg.matrix_rank(arr)
        print('Ранг матрицы', temp)
    elif num == '3x3':
        print('Введите элементы матрицы:')
        for i in range(9):
            n = int(input())
            arr = np.append(arr, n)
        arr.shape = (3, 3)
        temp = np.linalg.matrix_rank(arr)
        print('Ранг матрицы', temp)
