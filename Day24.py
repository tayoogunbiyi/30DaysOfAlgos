def compress_string(s):
    result = []
    curr_character_count = 1
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            result.append(s[i-1])
            result.append(str(curr_character_count))
            curr_character_count = 1
        else:
            curr_character_count+=1
    
    result.append(s[-1])
    result.append(str(curr_character_count))

    return ''.join(result)


print(compress_string('aaaabbbbccccdddd'))

print(compress_string('abccccbbbdbbaaaa'))

print(compress_string('weeecccdgeeeefggg'))

print(compress_string('abcd'))