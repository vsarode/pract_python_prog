from itertools import permutations


def inbuilt_permute(string):
    for o in permutations(string):
        print(''.join(o))


def permute(data, i, length):
    if i==length:
        print(''.join(data))
    else:
        for j in range(i,length):
            #swap
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            # data[i], data[j] = data[j], data[i]



if __name__ == '__main__':
    # print(inbuilt_permute('abc'))
    s = 'abcd'
    permute(list(s), 0, len(s))
