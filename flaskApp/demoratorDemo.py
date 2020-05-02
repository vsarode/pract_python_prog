def mydecorator(func):
    def wrapper(*args, **kwargs):
        if args[0] > 5:
            return func(*args, **kwargs)
        else:
            raise Exception

    return wrapper


@mydecorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    print add(4, 20)
