def retry(func):
    def wrap(*args, **kwargs):
        try:
            print 'calling'
            do()
        except ZeroDivisionError as e:
            wrap(*args, **kwargs)
    return wrap

@retry
def do():
    print 10 / 0


if __name__ == '__main__':
    do()
