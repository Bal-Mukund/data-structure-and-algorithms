"""  [ Question]   Write a function that takes in a non-empty array of integers
                    that are sorted in ascending order and returns a new array 
                    of the same length with the squares of the original integers
                    also sorted in ascending order. """


#  O(n)  Time | O(n) Space complexity 

array = [1]

def sortedSquaredArray(array):
    sqdarray= [None for _ in array]

    sqdindex = len(sqdarray) - 1
    start = 0
    end = len(array) - 1


    while start < end:
        start_value = array[start]
        end_value = array[end]

        if abs(end_value) > abs(start_value):
            sqdvalue = end_value * end_value

            sqdarray[sqdindex] = sqdvalue

            sqdindex -= 1
            end -= 1

        elif abs(start_value) > abs(end_value):
            sqdvalue = start_value * start_value

            sqdarray[sqdindex] = sqdvalue

            sqdindex -= 1
            start += 1

        elif abs(start_value) == abs(end_value):

            sqdvalue1 = start_value * start_value
            sqdvalue2 = end_value * end_value

            sqdarray[sqdindex] = sqdvalue1
            sqdarray[sqdindex - 1] = sqdvalue2

            sqdindex -= 2

            start += 1
            end -= 1
    if start == end:

        sqdvalue = array[start] * array[start]

        sqdarray[sqdindex] = sqdvalue

    return  sqdarray

print(sortedSquaredArray(array))
