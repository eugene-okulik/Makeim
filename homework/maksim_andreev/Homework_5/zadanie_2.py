rez1 = 'результат операции: 42'
rez2 = 'результат операции: 514'
rez3 = 'результат работы программы: 9'
place1 = rez1.index(':')
place2 = rez2.index(':')
place3 = rez3.index(':')
number1 = int(rez1[place1 + 1:])
number1plus10 = number1 + 10
number2 = int(rez2[place2 + 1:])
number2plus10 = number2 + 10
number3 = int(rez3[place3 + 1:])
number3plus10 = number3 + 10
print(number1plus10)
print(number2plus10)
print(number3plus10)
