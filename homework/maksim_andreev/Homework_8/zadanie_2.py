def fibonachi(limit):
    a, b = 0, 1
    count = 1
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


count = 1
for number in fibonachi(100001):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1
