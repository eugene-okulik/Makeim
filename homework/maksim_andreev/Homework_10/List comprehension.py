PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split()
new_set = [x.replace('р', '') if x.endswith('р') else x for x in new_list]
new_dict = dict(zip(new_set[::2], map(int, new_set[1::2])))
print(new_dict)
