List = list(range(1, 101))
for number in List:
    if number % 3 == 0:
        if number % 5 == 0:
            print('FuzzBuzz')
        else:
            print('fuzz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
