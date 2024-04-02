def finish(func):
    def wrapper(text):
        func(text)
        print('')
        print('finished')

    return wrapper


@finish
def example(text):
    print(text)


example('print me')
