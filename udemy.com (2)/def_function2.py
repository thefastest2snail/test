def rectangle():
    a = float(input('Shirina: '))
    b = float(input('Vysota: '))
    print('Ploshad: %.2f' % (a*b))

def triangle():
    a = float(input('Osnovanie: '))
    h = float(input('Vysota: '))
    print('Ploshad: %.2f' % (0.5 * a * h))

def circle():
    r = float(input('Radius: '))
    print('Ploshad: %.2f' % (3.14 * r * 2))

figure = input('1-rectangle, 2-triangle, 3-circle: ')
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print('Input error')
