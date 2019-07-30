#GOAL: Count the number of words of a text.

from collections import Counter  #counter is a sub class of dictionary.

def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary where keys are unique words
    and values are word counts
    :param text:
    :return:
    """
    word_counts = {}        # dictionary
    for word in text.split(' '):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        # unknown word
        else:
            word_counts[word] = 1

    # this function has the problem with upper case letter and punctuations which are included as part of the word
    return word_counts


def count_wordsv2(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary where keys are unique words
    and values are word counts. We make the input text into lower cases and the punctuations are skipped.
    :param text:
    :return:
    """
    text = text.lower()     # making all the text into lower case
    skips= ['.', ',', ';', ':', '"', "'"]

    for ch in skips:
        text = text.replace(ch, '')   # replacing the characters in the list, slips, with nothing

    print(text)

    word_counts = {}        # dictionary
    for word in text.split(' '):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        # unknown word
        else:
            word_counts[word] = 1

    return word_counts

def count_words_withCounter(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary where keys are unique words
    and values are word counts. We make the input text into lower cases and the punctuations are skipped.
    :param text:
    :return:
    """
    text = text.lower()     # making all the text into lower case
    skips= ['.', ',', ';', ':', '"', "'"]

    for ch in skips:
        text = text.replace(ch, '')   # replacing the characters in the list, slips, with nothing

    word_counts = Counter(text.split(' '))  #using a sub class of dictionary which counts

    return word_counts


text = "This is my test text. We're keeping this text short to keep things manageable. This is just a test we want to check."

dictionary = count_words(text)
print(dictionary)
dictionary = count_wordsv2(text)
print(dictionary)
counter = count_words_withCounter(text)
print(counter)

print(dictionary==counter)