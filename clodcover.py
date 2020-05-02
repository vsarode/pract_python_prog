
def is_y_at_start_or_end(word):
    return word[0] == 'y' or word[-1]=='y'
    is_y_at_start_or_end  = False
    if word[0] == 'y':
        is_y_at_start_or_end= True
    if word[-1] == 'y':
        is_y_at_start_or_end= True
    return is_y_at_start_or_end


def get_vowel_index(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for i, letter in enumerate(word):
        if letter in vowels:
            print("j", letter)
            if i == (len(word)-1):
                if i != 'y':
                    return i
    print(len(word))
    return -1

def is_vowel(letter, word):
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  return letter in vowels

def getRhymePattern(word):
  word = word[::-1]
  vowel_index = get_vowel_index(word)

  if vowel_index != -1:
    vowel_string = word[:vowel_index]
    print(word, "-", vowel_string)
    for i in range(vowel_index, len(word)):
      if is_vowel(word[i]):
        print(i, len(word)-1, word[i])
        if i != (len(word)-1) or word[i] != 'y':
            vowel_string += word[i]
        print("out->", vowel_string)
      else:
        break
    if vowel_string:
        # if vowel_string[len(vowel_string)-1] == 'y':
        #     vowel_string = vowel_string[:-1]
        return vowel_string[::-1]



if __name__ == '__main__':
    input = 'rhtyhm'
    print(is_y_at_start_or_end(input))
    # print(getRhymePattern(input))