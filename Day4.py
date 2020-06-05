def first_unique(string):
    frequency_map = {}
    for ch in string:
        frequency_map[ch] = frequency_map.get(ch, 0) + 1

    for i in range(len(string)):
        if frequency_map[string[i]] == 1:
            return i
    return -1

