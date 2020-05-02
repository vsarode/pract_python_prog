'''
Give n th fibonacci no.
'''
import time


def fib(n):
    if n == 1 or n == 2:
        result = 1;
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


def fib_memoizaion(n, mem):
    if mem[n] != None:
        return mem[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    mem[n] = result
    return result


def fib_bottome_up(n):
    if n == 1 or n == 2:
        return  1
    bottom_up = [None for i in range(n + 2)]
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


if __name__ == '__main__':
    start = time.time()
    n = 40
    # print fib_memoizaion(n, [None for n in range(n+1)])
    # print fib(n)
    print fib_bottome_up(n)
    # 102334155
    print time.time() - start
