'''
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


def is_unique(sub_str):
    m = {}
    for latter in sub_str:
        if latter in m:
            return False
        else:
            m[latter] = 1
    return True


def get_longest_substring_withoutrepeating_char(input_string):
    longest_subst_size = 0
    i, j = 0, 1
    while j <= len(input_string):
        print(i,j, is_unique(input_string[i:j]))
        if is_unique(input_string[i:j]):
            if longest_subst_size < j - i:
                print(input_string[i:j])
                longest_subst_size = j - i
        else:
            i += 1
            while i <= j:
                if not is_unique(input_string[i:j]):
                    i += 1
                else:
                    break

        j += 1
    return longest_subst_size


if __name__ == '__main__':
    s = 'aab'
    # s='abcabcbb'
    # s = 'dvdf'
    print(get_longest_substring_withoutrepeating_char(s))
