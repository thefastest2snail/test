try:
    n = input ('Введите целое число: ')
    n = int(n)
except ValueError:
    print('Вы что-то попутали с вводом')
else:
    print('Все нормально, вы ввели число', n)
finally:
    print ('Конец программы')
