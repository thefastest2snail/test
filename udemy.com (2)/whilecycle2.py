total = 100

while total > 0:
    n = int(input('enter the number: '))
    try:
        n = int(n)
        total = total - n
    except ValueError:
        print('Введите целое число!')
        n = int(input('enter the number: '))
    

print('Ресурс исчерпан')
