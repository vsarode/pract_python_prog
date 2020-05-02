'''
1
2 4           3         5
10 8 3       13 13    13  8
'''

"""
10 8 3

"""


def get_max_sum():
    array = [
        [1],
        [2, 4],
        [6, 8, 3],
        [10, 20, 30, 40]
    ]
    i = len(array) - 1
    while i > 0:
        for j in range(len(array[i - 1])):
            array[i - 1][j] = max(array[i - 1][j] + array[i][j], array[i - 1][j] + array[i][j + 1])
        i -= 1
    return array[0][0]


if __name__ == '__main__':
    print(get_max_sum())
