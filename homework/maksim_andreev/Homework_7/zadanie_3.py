rez1 = 'результат операции: 42'
rez2 = 'результат операции: 54'
rez3 = 'результат работы программы: 209'
rez4 = 'результат: 2'


def sentence(value):
    place = value.index(':')
    number = int(value[place + 1:])
    print(number + 10)


sentence(rez1)
sentence(rez2)
sentence(rez3)
sentence(rez4)

"""
можно всё то же самое укоротить например если напрямую при вызове функции в параметр вставить "результат..."
по примеру sentence('результат операции: 42'), таким образом мы исключим верхние 6 строк
получилось бы вот так:
def sentence(value):
    place = value.index(':')
    number = int(value[place + 1:])
    print(number + 10)


sentence('результат операции: 42')
sentence('результат операции: 54')
sentence('результат работы программы: 209')
sentence('результат: 2')
"""
