def cylinder():
    r = float(input('Радиус: '))
    h = float(input('Высота: '))
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return side, full

sCyl, fCyl = cylinder()
print('Площадь боковой поверхности %.2f' % sCyl)
print('Полная площадь %.2f' % fCyl)
