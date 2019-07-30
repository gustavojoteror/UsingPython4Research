# Character encoding refers t othe process how computer encodes certain characters.
# this case we will use ITF-8 encoding which is the dominant character encoding for the web.

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

# let's read romeo and juliet
text = read_book('./Books/English/shakespeare/Romeo and Juliet.txt')
print(len(text))
phrase_text= ("What's in a name")
ind=text.find(phrase_text)
print(ind)
sample_text= text[ind:ind+1000]
print(sample_text)