n = float(input())
minimum = n
maximum = n
i = 1
while i < 6:
    n = float(input())
    if n < minimum:
        minimum = n
    elif n > maximum:
        maximum = n
    i += 1
print('Minimum -', round(minimum, 2))
print('Maximum -', round(maximum, 2))
        
        
