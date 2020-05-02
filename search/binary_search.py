def binary_search_iterative(l, k):
    pass


def binary_search(l, s, e, k):
    if s < e:
        mid = (s + e) / 2
        if l[mid] == k:
            return mid
        if l[mid] > k:
            return binary_search(l, s, mid, k)
        else:
            return binary_search(l, mid + 1, e, k)
    return None


def binarySearch(arr, k, l, r):
    if l < r:
        m = (l + r) / 2
        if arr[m] == k:
            return m
        if arr[m] > k:
            return binarySearch(arr, k, l, m)
        else:
            return binarySearch(arr, k, m + 1, r)
    return None


if __name__ == '__main__':
    l = range(20)
    print l
    print binarySearch(l, 6, 0, len(l))
