def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for a in range(count):
            func(*args, **kwargs)
            print('')

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
