def printMaximum(num):
    # Hashed array to store count of digits
    count = [0 for x in range(10)]

    # Connverting given number to string
    string = str(num)

    # Updating the count array
    for i in range(len(string)):
        print(int(string[i]))
        count[int(string[i])] = count[int(string[i])] + 1

    # Result stores final number
    result = 0
    multiplier = 1

    # traversing the count array
    # to calculate the maximum number
    print(count)
    for i in range(10):
        while count[i] > 0:
            result = result + (i * multiplier)
            print('-',result)
            count[i] = count[i] - 1
            print('c',count[i])
            multiplier = multiplier * 10
            print('m', multiplier)

    # return the result
    return result

if __name__ == '__main__':
    print(printMaximum(132446578))