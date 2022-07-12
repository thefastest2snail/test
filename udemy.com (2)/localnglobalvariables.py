result = 0
def rectangle():
    a = float(input('Ширина: '))
    b = float(input('Длина: '))
    global result
    result= a*b

def triangle():
    a = float(input('Основание: '))
    h = float(input('Высота: '))
    global result
    result = 0.5 * a * h

figure = input('1-rectangle, 2-triangle: ')
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
    
print ('Площадь: %.2f' % result)
