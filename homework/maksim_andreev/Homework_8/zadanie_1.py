import random

bonus = random.choice([True, False])
salary = int(input('Enter your salary: '))
sumofbonus = random.randint(1, 10000)

if bonus is True:
    equals = salary + sumofbonus
else:
    equals = salary
print(f'{salary}, {bonus} - ${equals}')
