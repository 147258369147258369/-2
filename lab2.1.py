op = input('Выберите операцию: транспонирование, умножение, нахождение ранга ')
if op != 'нахождение ранга':
    op1 = input('Выберите размер матрицы: 1x2, 2x1, 1x3, 3x1, 2x2, 3x3 ')
else:
    op1 = input('Выберите размер матрицы: 2x2, 3x3 ')
a, b, c, d, e = [], [], [], [], []
count = 0
count1 = 0
if op == 'транспонирование':
    print('вводите элементы матрицы построчно: ')
    if op1 == '1x2':
        a.append(int(input()))
        b.append(int(input()))
        print(a, b, sep='\n')
    if op1 == '1x3':
        a.append(int(input()))
        b.append(int(input()))
        c.append(int(input()))
        print(a, b, c, sep='\n')
    if op1 == '2x1':
        for i in range(2):
            a.append(int(input()))
        print(a)
    if op1 == '3x1':
        for i in range(3):
            a.append(int(input()))
        print(a)
    if op1 == '2x2':
        for i in range(2):
            a.append(int(input()))
        for i in range(2):
            b.append(int(input()))
        a[1], b[0] = b[0], a[1]
        print(a, b, sep='\n')
    if op1 == '3x3':
        for i in range(3):
            a.append(int(input()))
        for i in range(3):
            b.append(int(input()))
        for i in range(3):
            c.append(int(input()))
        a[1], b[0] = b[0], a[1]
        a[2], c[0] = c[0], a[2]
        c[1], b[2] = b[2], c[1]
        print(a, b, c, sep='\n')
if op == 'умножение':
    op2 = input('Выберите размер второй матрицы: 1x2, 2x1, 1x3, 3x1, 2x2, 3x3 ')
    if op1 == '1x2':
        for i in range(2):
            a.append(int(input('Введите элементы первой матрицы построчно: ')))
        if op2 == '2x1':
            for i in range(2):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d = [a[0]*b[0]+a[1]*b[1]]
            print(d)
        if op2 == '2x2':
            for i in range(4):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d = [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3]]
            print(d)
        else:
            print('Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
    elif op1 == '2x1':
        for i in range(2):
            a.append(int(input('Введите элементы первой матрицы построчно: ')))
        if op2 == '1x2':
            for i in range(2):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c = [a[0]*b[0], a[0]*b[1]], [a[1]*b[0], a[1]*b[1]]
            print(d, c, sep='\n')
        if op2 == '1x3':
            for i in range(3):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c = [a[0]*b[0], a[0]*b[1], a[0]*b[2]], [a[1]*b[0], a[1]*b[1], a[1]*b[2]]
            print(d, c, sep='\n')
        else:
            print('Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
    elif op1 == '1x3':
        for i in range(3):
            a.append(int(input('Введите элементы первой матрицы построчно: ')))
        if op2 == '3x1':
            for i in range(3):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d = [a[0]*b[0]+a[1]*b[1]+a[2]*b[2]]
            print(d)
        elif op2 == '3x3':
            for i in range(9):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d = [a[0]*b[0]+a[1]*b[3]+a[2]*b[6], a[0]*b[1]+a[1]*b[4]+a[2]*b[7], a[0]*b[2]+a[1]*b[5]+a[2]*b[8]]
            print(d)
        else:
            print('Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
    elif op1 == '3x1':
        for i in range(3):
            a.append(int(input('Введите элементы первой матрицы построчно: ')))
        if op2 == '1x2':
            for i in range(2):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c, e = [a[0]*b[0], a[0]*b[1]], [a[1]*b[0], a[1]*b[1]], [a[2]*b[0], a[2]*b[1]]
            print(d, c, e, sep='\n')
        if op2 == '1x3':
            for i in range(3):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c, e = [a[0]*b[0], a[0]*b[1], a[0]*b[2]], [a[1]*b[0], a[1]*b[1], a[1]*b[2]], [a[2]*b[0], a[2]*b[1], a[2]*b[2]]
            print(d, c, e, sep='\n')
        else:
            print('Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
    elif op1 == '2x2':
        for i in range(4):
            a.append(int(input('Введите элементы первой матрицы построчно: ')))
        if op2 == '2x1':
            for i in range(2):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c = [a[0]*b[0]+a[1]*b[1]], [a[2]*b[0]+a[3]*b[1]]
            print(d, c, sep='\n')
        if op2 == '2x2':
            for i in range(4):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c, = [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3]], [a[2]*b[0]+a[3]*b[2], a[2]*b[3]+a[3]*b[3]]
            print(d, c, sep='\n')
        else:
            print('Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
    elif op1 == '3x3':
        for i in range(9):
            a.append(int(input('Введите элементы первой матрицы построчно: ')))
        if op2 == '3x1':
            for i in range(3):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            d, c, e = [a[0]*b[0]+a[1]*b[1]+a[2]*b[2]], [a[3]*b[0]+a[4]*b[1]+a[5]*b[2]], [a[6]*b[0]+a[7]*b[1]+a[8]*b[2]]
            print(d, c, e, sep='\n')
        if op2 == '3x3':
            for i in range(9):
                b.append(int(input('Введите элементы второй матрицы построчно: ')))
            c = [[a[0]*b[0]+a[1]*b[3]+a[2]*b[6]], [a[0]*b[1]+a[1]*b[4]+a[2]*b[7]], [a[0]*b[2]+a[1]*b[5]+a[2]*b[8]]]
            d = [[a[3]*b[0]+a[4]*b[3]+a[5]*b[6]], [a[3]*b[1]+a[4]*b[4]+a[5]*b[7]], [a[3]*b[2]+a[4]*b[5]+a[5]*b[8]]]
            e = [[a[6]*b[0]+a[7]*b[3]+a[8]*b[6]], [a[6]*b[1]+a[7]*b[4]+a[8]*b[7]], [a[6]*b[2]+a[7]*b[5]+a[8]*b[8]]]
            print(c, d, e, sep='\n')
    else:
        print('Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй матрицы.')
if op == 'нахождение ранга':
    if op1 == '2x2':
        for i in range(4):
            k = int(input('Введите элементы первой матрицы построчно: '))
            a.append(k)
            if k == 0:
                count += 1
        if count == 4:
            print('Ранг матрицы равен 0')
        elif a[0]*a[3]-a[1]*a[2] == 0:
            print('Ранг матрицы равен 1')
        else:
            print('Ранг матрицы равен 2')
    if op1 == '3x3':
        for i in range(9):
            k = int(input('Введите элементы  матрицы построчно: '))
            a.append(k)
            if k == 0:
                count += 1
        if a[0]*a[4]-a[1]*a[3] == 0:
            count1 += 1
        if a[1]*a[5]-a[2]*a[4] == 0:
            count1 += 1
        if a[3]*a[7]-a[4]*a[6] == 0:
            count1 += 1
        if a[4]*a[8]-a[5]*a[7] == 0:
            count1 += 1
        if count == 9:
            print('Ранг матрицы равен 0')
        elif count1 == 4:
            print('Ранг матрицы равен 1')
        elif a[0]*a[4]*a[8]+a[1]*a[5]*a[6]+a[3]*a[7]*a[2]-(a[2]*a[4]*a[6]+a[1]*a[3]*a[8]+a[0]*a[5]*a[7]) != 0:
            print('Ранг матрицы равен 3')
        else:
            print('Ранг матрицы равен 2')
