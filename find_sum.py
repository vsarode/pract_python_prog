def is_present(l, )
def find_sum(l1, l2, sum):
    sorted_l2 = sorted(l2)
    for i in range(len(l1)):
        is_present, index2 = is_present(sorted_l2, sum-l1[i ])
        if is_present:
            return i, index2
