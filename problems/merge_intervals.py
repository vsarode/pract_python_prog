def is_overlapping(intervals, start):
    for i, v in enumerate(intervals):
        if v[0] < start < v[1]:
            return True, i

    return False, None


def merge_intervals(intervals):
    response = []
    for i in range(len(intervals)):
        is_overlaping, index = is_overlapping(intervals, intervals[i][0])
        if is_overlaping:
            pair = intervals[i]
            to_be_adjust = intervals[index]
            new_pair = (to_be_adjust[0], pair[1])
            if to_be_adjust in response:
                response.remove(to_be_adjust)
            if new_pair not in response:
                response.append(new_pair)
        else:
            response.append((intervals[i][0], intervals[i][1]))

    return response


if __name__ == '__main__':
    # print is_overlapping([(100, 200), (150, 300),(400, 500), (350, 399)], 150)
    print merge_intervals([(100, 200), (400, 500), (150, 300), (350, 399)])
