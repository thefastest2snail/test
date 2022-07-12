print('Это программа для опеределения площади цилиндра, следуйте дальнейшим инструкциям.')

result = 0

def cylinder_full_area():
    a = float(input('Введите радиус цилиндра: '))
    global result
    result = 3.14 * a ** 2

def cylinder_side_area():
    a = float(input('Введите радиус цилиндра: '))
    b = float(input('Введите высоту цилиндра: '))
    global result
    result = 3.14 * a * b

figure = input('Введите числовой код для определения конкретной площади цилиндра. 1-площадь боковой поверхности цилиндра, 2-полная площадь цилиндра: ')
if figure == '1':
    cylinder_side_area()
elif figure == '2':
    cylinder_full_area()


print ('Площадь: %.2f' % result)
    
