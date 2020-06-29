def has_all_unique_characters(s):
    seen_characters = set()
    for char in s:
        if char in s:
            return False
        seen_characters.add(s)

    return True
