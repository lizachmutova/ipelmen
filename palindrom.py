
def palindrom():
    s = input('Введите слово:')
    a = s[::-1]
    if a ==s:
        print(True)
    else:
        print(False)
palindrom()

