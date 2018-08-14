from collections import defaultdict
from string import ascii_lowercase


def count_words(string):

    word_dict = defaultdict(int)

    words = string.split(' ')

    for word in words:

        word = ''.join(char
                       for char in word.lower()
                       if char in ascii_lowercase + "'")

        word_dict[word] += 1

    return word_dict
