from collections import Counter  #counter is a sub class of dictionary.
from functions import *

def word_stats(word_counts):
    """
    Return number of unique words and word frequencies.
    :param word_counts:
    :return:
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


print('English Romeo and Juliet')
text = read_book('./Books/English/shakespeare/Romeo and Juliet.txt')
print(len(text))
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)

print(num_unique)  # number of unique words in the book
print(sum(counts)) # total words in the book

print('German Romeo and Juliet')
text = read_book('./Books/German/shakespeare/Romeo und Julia.txt')
print(len(text))
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)

print(num_unique)  # number of unique words in the book
print(sum(counts)) # total words in the book
