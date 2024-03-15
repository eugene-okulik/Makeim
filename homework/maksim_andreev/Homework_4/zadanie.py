my_dict = {'list': [1, 3, 8, 'log', False],
           'tuple': (4, 'soft', 42.5, True, 12),
           'dict': {'first': 1, 'second': 'malina', 'third': 91.1, 4: 23, True: False},
           'set': {'raz', 2, 44.5, 12, True}}

print(my_dict['tuple'][-1])
my_dict['list'].append(50)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'randomvalue'
my_dict['dict'].pop(4)
my_dict['set'].add(50)
my_dict['set'].remove('raz')
print(my_dict)
