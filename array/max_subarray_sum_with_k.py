def get_sum_with_subarray_of_size_k(arr, k):
    max_sum = arr[0]
    i, j = 0, 1
    while j < len(arr)+1:
        if j - i > k:
            i += 1
        if max_sum < sum(arr[i: j]):
            max_sum = sum(arr[i: j])
        j += 1
    return max_sum


if __name__ == '__main__':
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    print(get_sum_with_subarray_of_size_k(arr, k))
