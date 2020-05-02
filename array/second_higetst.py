def second_highest(l):
    first = l[0]
    second = l[0]
    for i in l:
        if i > second:
            if i > first:
                second = first
                first = i
            else:
                second = i
    return first, second


if __name__ == '__main__':
    l = [10, 20, 1, 2, 3, 5, 60, 3, 20, 50]
    print(second_highest(l))
