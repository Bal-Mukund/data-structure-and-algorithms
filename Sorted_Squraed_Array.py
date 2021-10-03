""" [Question]  Write a function that takes in a non-empty array of integers that 
                are sorted in ascending order and returns a new array of the same length 
                with the squares of the original integers also sorted in ascending order. """



#   O(nlogn)  Time | O(n) Space Complexity 


def sortedSquaredArray(array):
    sqd = []

    for value in array:
        sqd.append(value * value)

    return sorted(sqd)
