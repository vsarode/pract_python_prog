def longcp(strs):
    longest_pref = ""
    i = 0
    while True:
        for j in range(len(strs) ):
            try:
                print(strs[j][i], strs[j+1][i])
                if strs[j][i] != strs[j + 1][i]:
                    return longest_pref
            except:
                return longest_pref
            longest_pref += strs[0][i]
            i += 1
    return longest_pref


if __name__ == '__main__':
    i = ["flower", "flow", "flight"]
    print(longcp(i))
