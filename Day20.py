def is_string_rotation(s1,s2):
    if len(s2) == len(s1):
        s1s1 = s1 + s1
        return s2 in s1s1
    return False
