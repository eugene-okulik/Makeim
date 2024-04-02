def operation_decorator(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'

        return func(first, second, operation)
    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first * second


first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
result = calc(first, second)
print(result)
