def function():
    a = int(input('Введите число 1: '))
    b = int(input('Введите число 2: '))
    while a != 0 and b != 0:
        c = a * b
        print ('Значение умножения двух чисел равен ', c)
        a = int(input('Введите число 1: '))
        b = int(input('Введите число 2: '))
        
    print ('Один из введенных чисел равен нулю') 
c = function()

        
