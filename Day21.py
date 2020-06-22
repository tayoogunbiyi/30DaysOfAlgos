def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(list(s1))
    s2 = sorted(list(s2))

    s1 = ''.join(s1)
    s2 = ''.join(s2)

    return s1 == s2


def are_anagrams_2(s1,s2):
    if len(s1) != len(s2):
        return False
    
    count_map = {}

    for char in s1:
        count_map[char] = count_map.get(char,0) + 1
    
    for char in s2:
        count_map[char] = count_map.get(char,0) - 1
        if count_map[char] < 0:
            return False
    return True



print(are_anagrams("hello","world"))
print(are_anagrams("hello","olleh"))

# print(are_anagrams_2('fired','fried'))