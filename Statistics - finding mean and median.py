"""Write a function that accepts a tuple of positive integers and returns the mean and median of the integers as
a tuple. For example if the input tuple is:
(3, 3, 0, 1, 12, 13, 15, 16)
then your function should return a tuple that contains the mean and median as:
(7.875, 7.5)
Use the "statistics" module. """

# imo, it may be better to input a list instead of a tuple


values = [3, 3, 0, 1, 12, 13, 15, 16]

from statistics import *

def meanAndmedian(listItems):
    x = mean(listItems)
    y = median(listItems)
    print((x, y))


meanAndmedian(values)



