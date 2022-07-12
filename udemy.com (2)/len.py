c = input('Введите любую строку: ')
if len(c) > 10:
    print ('В строке больше 10 символов')
else:
    diff = 10 - len(c)
    c = c + '*' * diff
    print(c)
    
