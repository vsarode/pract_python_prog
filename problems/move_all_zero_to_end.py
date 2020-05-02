def move_all_zero(arr):
    count_of_zero = 0
    for a in arr:
        if a == 0:
            count_of_zero += 1
    res = filter(lambda x: not x == 0, arr)
    res.extend([0 for x in range(count_of_zero)])
    return res


if __name__ == '__main__':
    arr = [6, 0, 2, 3, 4, 0, 1, 0]
    print move_all_zero(arr)
