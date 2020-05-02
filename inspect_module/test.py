import inspect

import demo

if __name__ == '__main__':

    for name, data in inspect.getmembers(demo.X, inspect.ismethod):
        if name.startswith('__'):
            continue
        print('{} : {!r}'.format(name, data))
        print type(data)
        # print isinstance(demo.X, data)
