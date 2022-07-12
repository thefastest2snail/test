total = int(input('Введите целое число для подсчета: '))

i = 0
n = 0
while i < 20 and n < 20:
    n += 1
    total =total**(2+n)
    i += 1
    print (total)
print ('Расчет окончен')

