try:
    n = input ('Введите целое число: ')
    n = int(n)
except ValueError:
    print('Вы что-то попутали с вводом')
    try:
        3 / 0
    except ZeroDivisionError:
        print ('Деление на ноль')
else:
    print('Все нормально, вы ввели число', n)
finally:
    print('Конец программы')
