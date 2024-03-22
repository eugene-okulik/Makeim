a = 10
while True:
    b = int(input('Введите число: '))
    if b != a:
        print('попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
