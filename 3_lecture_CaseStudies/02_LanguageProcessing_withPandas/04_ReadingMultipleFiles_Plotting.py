#Being able to navigate file directories is very important.
# the goal of this script is to read every book contained in the various subdirectories of the book folder.

from collections import Counter  #counter is a sub class of dictionary.
from functions import *
import os
import pandas as pd
import matplotlib.pyplot as plt

dir = os.getcwd()           # to get the current directory
book_dir = dir+"/Books"
print('The current directory is: ', dir)

# creating an empty table
stats =pd.DataFrame(columns= ('language', 'author', 'title', 'length', 'unique'))
title_num = 1   #to count the number of rows
for language in os.listdir(book_dir):  # returns a list of directories:
    # loops over all languages
    for author in os.listdir(book_dir+ "/" + language):
        # loops over all authors
        for title in os.listdir(book_dir+ "/" + language + "/" + author):
            # loops over all title
            inputfile = book_dir+ "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))

            #introducing data to able data frame or table
            # stats.loc[title_num] = language, author, title, sum(counts), num_unique
              # capitalizing the name of the author and removing the ,txt at the end of the book
            stats.loc[title_num] = language, author.capitalize(), title.replace('.txt', ''), sum(counts), num_unique

            title_num += 1


print(stats.head())     # first 5 lines of the table
print(stats.tail())     # last 5 lines of the table

print(stats.length)     # we can access the data depending on the title
print(stats.unique)


# stats_German = stats[stats.language =='German']
# stats_Portuguese = stats[stats.language =='Portuguese']
# stats_French = stats[stats.language =='French']

#for more colors: google: "html colors"  (https://www.rapidtables.com/web/color/html-color-codes.html)

plt.figure(figsize= (10,10))
subset = stats[stats.language =='English']
plt.loglog(subset.length, subset.unique, 'o', label='English', color= 'crimson')

subset = stats[stats.language =='French']
plt.loglog(subset.length, subset.unique, 'o', label='French', color= 'green')

subset = stats[stats.language =='German']
plt.loglog(subset.length, subset.unique, 'o', label='German', color= 'orange')

subset = stats[stats.language =='Portuguese']
plt.loglog(subset.length, subset.unique, 'o', label='Portuguese', color= 'blueviolet')
plt.legend()
plt.xlabel('Book length')
plt.ylabel('Number of unique words')
plt.show()
plt.savefig('book_stats.pdf')