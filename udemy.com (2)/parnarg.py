def cylinder(h, r = 1):
    side = 2 * 3.14 * r * h
    circle = 3.14 * r**2
    full = side + 2 * circle
    return full
a = float(input('Введите первый аргумент: '))
b = float(input('Введите второй аргумент: '))

figure1 = cylinder(a, b)
figure2 = cylinder(5)
figure3 = cylinder(10, 2)
figure4 = cylinder(r = 2, h = 10)
print(figure1)
print(figure2)
print(figure3)
print(figure4)
