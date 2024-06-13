def create_dictionary(word):
    new_dictionary = {}
    for i in word:
        count = 0
        for j in word:
            if i == j:
                count += 1
        new_dictionary.update({i: count})
    return new_dictionary

print(create_dictionary("w3school"))