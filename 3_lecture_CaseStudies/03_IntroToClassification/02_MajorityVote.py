# Majority vote (o plurality vote): given an array or a sequence of votes (e.g. 1,2, 4, 2) we need to determine
# how many times each occurs, and then find the most common element. For the case above the majority vote is 2
# The return is not the amount of times the elements is there, however the observation corresponding to the highest count. WHo got it?

import random
import scipy.stats as ss

def majority_vote(votes):
    """
    Returns the most common element in votes
    Count the number of votes each word occurs in text (str). Return dictionary where keys are unique words
    and values are word counts. We make the input text into lower cases and the punctuations are skipped.
    This function calcualtes what is called in statistics as mode.
    :param vote:
    :return:
    """

    vote_counts = {}        # dictionary
    for vote in votes:
        # known word
        if vote in vote_counts:
            vote_counts[vote] += 1
        # unknown word
        else:
            vote_counts[vote] = 1

    print(vote_counts)
    # but who is the winner?
    winners = []
    max_votes = max(vote_counts.values())

    # for (,) this is a tuple
    for vote, count in vote_counts.items():
        if count == max_votes:
            winners.append(vote)

    # what is we have multiply winners? Well we select one randomly

    return random.choice(winners)

def majority_vote_scipy(votes):
    """
    Google how to calculate the mode of a numpy array in google: scipy.mstats.mode()
    Returns the most common element in votes
    This function only works with floats
    :param vote:
    :return:
    """

    mode, count = ss.mstats.mode(votes)


    return mode



# votes = ['gus','gus','otero','otero','jose','otero','otero','jose','gus','gus','gus','jose','otero','otero','jose','otero','gus','gus','gus']
votes = [1,1,3,3,2,3,3,2,1,1,1,2,3,3,2,3,1,1,1]

winner = majority_vote(votes)
winner2 = majority_vote_scipy(votes)

print(winner)
print(winner2)
# print(max(vote_counts))  #   the one that has the most repetition.       same as print(max(vote_counts.keys()))
# print(max(vote_counts.values()))  # the most repetition

