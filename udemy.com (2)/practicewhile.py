total = 100

while total > 0:
    n = int(input('Введите любое целое число: '))
    total -= n
    if total < 0:
        print ('Общее значение ушло в минус!')

print ('Недопустимая операция')
 
