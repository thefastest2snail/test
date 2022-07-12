def getInput():
    s = input()
    return s

def testInput(s):
    try:
        n = int(s)
        return True
    except ValueError:
        return False

def strToInt(s):
    n = int(s)
    return n

def printInt(n):
    print(n)

s1 = getInput()
is_int = testInput(s1)
if is_int == True:
    n1 = strToInt(s1)
    printInt(n1)
