def most_common_word(sentence):
    if not sentence:
        return ''
    word_list = sentence.split(' ')
    ht = {}
    for word in word_list:
        ht[word] = ht.get(word, 0)+1

    max_so_far = ht[word_list[0]]
    best_word = word_list[0]
    for i in range(1, len(word_list)):
        word = word_list[i]
        if ht[word] > max_so_far:
            max_so_far = ht[word]
            best_word = word

    return best_word


print(most_common_word("Hey cow brown cow"))
print(most_common_word("Hey now brown cow"))
