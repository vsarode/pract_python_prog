import sys


def is_sorted_rotated(arr):
    max = sys.maxint
    r = 0
    pivote = 0
    for i in range(len(arr) - 1):
        if not arr[i] < arr[i + 1] and not arr[i] < max and not r <= 2:
            return "NO", max
        if arr[i] > arr[i + 1]:
            r += 1
            pivote = i
        if r > 1:
            return "NO", max
    return "YES", min(pivote + 1, len(arr)-(pivote+1))


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 8, 1, 2, 3]
    print is_sorted_rotated(arr)
