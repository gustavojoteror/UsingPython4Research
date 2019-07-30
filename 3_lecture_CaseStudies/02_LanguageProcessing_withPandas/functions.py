from collections import Counter  #counter is a sub class of dictionary.

def count_words(text):
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


def read_book(title_path):
    """
    Read a book and terun it as a string
    :param title_path:
    :return: text
    """

    with open(title_path, 'r', encoding='utf8') as current_file:
        text= current_file.read()
        # see previous code to see why this is necessary
        text= text.replace('\n','').replace('\r','')   # we can put a replace after the other

    return text


def word_stats(word_counts):
    """
    Return number of unique words and word frequencies.
    :param word_counts:
    :return:
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)