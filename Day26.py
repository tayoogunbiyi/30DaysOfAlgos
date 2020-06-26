import collections
def is_pallindrome_permutation(s):
    count_map = collections.Counter(s)
    seen_single_char = False

    for key in count_map:
        occurences = count_map[key]
        if occurences % 2 == 1:
            if seen_single_char:
                return False
            seen_single_char = True
    return True


print(is_pallindrome_permutation('aba'))
print(is_pallindrome_permutation('aab'))
print(is_pallindrome_permutation('mama'))


        