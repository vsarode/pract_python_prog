def get_max_earning(pickup, drop, tip):
    ref_map = {}
    for i in range(len(pickup)):
        # print i
        earning = drop[i] - pickup[i] + tip[i]
        add = True
        for key, val in ref_map.iteritems():
            # print key, val, pickup[i]
            if key < pickup[i] < val[0] and val[1] < earning:
                ref_map.pop(key)
                ref_map[pickup[i]] = [drop[i], earning]

            elif key < pickup[i] < val[0] and val[1] > earning:
                add = False
            if key == pickup[i]:
                if val[1] < earning:
                    ref_map.pop(key)
                    ref_map[pickup[i]] = [drop[i], earning]
                else:
                    add=False
        if add:
            ref_map[pickup[i]] = [drop[i], earning]
    return sum([x[1] for x in ref_map.values()])


if __name__ == '__main__':
    pickup = [0, 2, 9, 10, 11, 12]
    drop = [5, 9, 11, 11, 14, 17]
    tip = [1, 2, 3, 2, 2, 1]
    # [6, 9, 5, 3, 5, 6]

    # pickup = [0, 0, 4, 5]
    # drop = [3, 2, 5, 7]
    # tip = [1, 1, 2, 2]

    # pickup  = [1,4]
    # drop    = [5,6]
    # tip     = [2,5]
    print get_max_earning(pickup, drop, tip)
