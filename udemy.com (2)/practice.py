try:
    a = input('Первое значение: ')
    b = input('Второе значение: ')
    c = (float(a) + float(b))
except ValueError:
    print ('Результат:', a + b)
else:
    print ('Результат:', c)
