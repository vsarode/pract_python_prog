def canTravelLeft(i, j, arr, visited):

    return j > 0 and ((arr[i][j - 1]) != 0) and ((i, j - 1) not in visited)


def canTravelRight(i, j, arr, visited):

    return j < (len(arr[0]) - 1) and (arr[i][j + 1] != 0) and (
                (i, j + 1) not in visited)


def canTravelUp(i, j, arr, visited):
    return i > 0 and (arr[i - 1][j] != 0) and ((i - 1, j) not in visited)

def canTravelDown(i, j, arr, visited):
    return i < (len(arr[0]) - 1) and (arr[i + 1][j] != 0) and (
                (i + 1, j) not in visited)
def f(i, j, arr, l, r, u, d, index_visited):

    if i < len(arr) and j < len(arr[0]) and arr[i][j] == 9:
        return max(l, r, u, d)

    index_visited.append((i, j))
if (canTravelLeft(i, j, arr, index_visited)):
        left = f(i, j - 1, arr, l + 1, r, u, d, index_visited)
        index_visited = [(i, j), (i, j - 1)]
    else:
        left = -1

if (canTravelRight(i, j, arr, index_visited)):
    right = f(i, j + 1, arr, l, r + 1, u, d, index_visited)
    index_visited = [(i, j), (i, j + 1)]
    else:
        right = -1

if (canTravelUp(i, j, arr, index_visited)):
    up = f(i - 1, j, arr, l, r, u + 1, d, index_visited)
    index_visited = [(i, j), (i - 1, j)]
    else:
        up = -1

if (canTravelDown(i, j, arr, index_visited)):
    down = f(i + 1, j, arr, l, r, u, d + 1, index_visited)
    else:
        down = -1
        return max(left, right, up, down)

if __name__ == '__main__':
    arr = [[1, 1, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 1, 9, 1]]
print f(0, 0, arr, 0, 0, 0, 0, [])
