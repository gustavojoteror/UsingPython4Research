#GOAL to calculate the distance between to points
import numpy as np

p1 = np.array([0.4,40])
p2 = np.array([4,-4])

# next line does:
#   1. takes the difference between the points p2-p1 = [3,3]
#   2. takes the square of the difference between the points (p2-p1)^2 = [9,9]
#   3. sum this two guys together = 9 + 9 =18
#   4. takes the dthge sqrt root of the value: sqrt(18) = 4.24...
np.sqrt(np.sum(np.power(p2-p1, 2)))

# let's write this as a function

def distance(p1, p2):
    """
    Finds the distance between p1 and p2
    :param p1:
    :param p2:
    :return distance:
    """
    return np.sqrt(np.sum(np.power(p2-p1, 2)))

print(distance(p1, p2))