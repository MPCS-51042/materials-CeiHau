def fill_completions(fd):
    from string import punctuation
    documents = fd.read()
    words_lst = documents.split()
    # Pre-process the data
    new_words_lst = []
    for index, word in enumerate(words_lst):
        word = word.lower()  # all letters are lowercase
        word = word.strip(punctuation)  # Words are stripped of leading and trailing punctuation

        # Words containing non-alphabetic characters are ignored, as are words of length 1
        if word.isalpha() and (len(word) != 1):
            new_words_lst.append(word)

    #Create the dictionary
    dictionary = {}
    for word in new_words_lst:
        for index, letter in enumerate(word):
            if (index, letter) not in dictionary:
                dictionary[index, letter] = {word}
            else:
                dictionary[index, letter].add(word)
    return dictionary


def find_completions(prefix, c_dict):
    for index, letter in enumerate(prefix):
        if index == 0:
            result_set = c_dict[index, letter]
        else:
            result_set = result_set & c_dict[index, letter]
    return result_set


def main():
    pass


if __name__ == '__main__':
    from string import punctuation
    main()
    f = open("articles.txt")

    documents = f.read()
    print(type(documents))
    print(len(documents))

    words_lst = documents.split()
    print('TEST: a in list', 'a' in words_lst)

    new_words_lst = []
    for index, word in enumerate(words_lst):
        word = word.lower()  # all letters are lowercase
        #word = word.strip()
        word = word.strip(punctuation)  # Words are stripped of leading and trailing punctuation
        #Words containing non-alphabetic characters are ignored, as are words of length 1
        if  word.isalpha() and(len(word) != 1):
            new_words_lst.append(word)

    print('TEST: a in list', 'i' in new_words_lst)
    dictionary = {}
    for word in new_words_lst:
        if word.isalpha() == False:
            print("@@@@@@@@@@@@@@@@")
        for index, letter in enumerate(word):
            if (index, letter) not in dictionary:
                dictionary[(index, letter)] = {word}
            else:
                dictionary[(index, letter)].add(word)

    print(dictionary.keys())
    print(len(dictionary))
    print(dictionary[0,'a'])
    prefix = 'multis'
    for index, letter in enumerate(prefix):
        if index == 0:
            result_set = dictionary[index, letter]
        else:
            result_set = result_set & dictionary[index, letter]
    print(result_set)

    f.close()
    s = 'Ac\'A'
    s = s.lower()
    print(s)
    print(f"s is alpha {s.isalpha()}")
    d = {}
    print(len(d))
    c = "ñ"
    print(c.isalpha())

    #3h