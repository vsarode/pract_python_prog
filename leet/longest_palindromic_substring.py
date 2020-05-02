'''
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


def is_palindrom(sub_str):
    return sub_str == sub_str[::-1]


def get_longest_palindromic_substring(input_string):
    longest_subst_size = 0
    i, j = 0, 1
    while j <= len(input_string):
        print(i, j, is_palindrom(input_string[i:j]))
        if is_palindrom(input_string[i:j]):
            if longest_subst_size < j - i:
                print(input_string[i:j])
                longest_subst_size = j - i
        else:
            i += 1
            while i <= j:
                if not is_palindrom(input_string[i:j]):
                    i += 1
                else:
                    break

        j += 1
    return longest_subst_size


if __name__ == '__main__':
    s = 'babad'
    # s='abcabcbb'
    # s = 'dvdf'
    print(get_longest_palindromic_substring(s))
