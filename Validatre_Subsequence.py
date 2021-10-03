""" [Queston]  Given two non-empty arrays of integers, write a function that
               determines whether the second array is a subsequence of the first one. """



def isValidSubsequence(array, sequence):
    subidx = 0

    for value in array:

        if subidx == len(sequence):
            return True

    if value == sequence[subidx]:


        subidx += 1

    return subidx == len(sequence)
