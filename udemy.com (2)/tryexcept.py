try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    c = a/b
    print('Частное: %.2F' % c)
except (ValueError, ZeroDivisionError):
    print ('Нельзя вводить строки')
    print ('или делить на ноль')
