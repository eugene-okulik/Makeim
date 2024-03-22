count = 0
result = []
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key in words:
    while count < words[key]:
        result.append(key)
        count += 1
    count = 0
    result.append('\n')
print(''.join(result))
