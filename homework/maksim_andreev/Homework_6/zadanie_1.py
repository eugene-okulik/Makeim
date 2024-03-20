text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
List = text.split()
for eto in List:
    if eto.endswith('.'):
        print(eto.replace('.', 'ing.'), end=' ')
    elif eto.endswith(','):
        print(eto.replace(',', 'ing,'), end=' ')
    else:
        print(eto + 'ing', end=' ')

