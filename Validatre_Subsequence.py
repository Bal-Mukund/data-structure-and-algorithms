def isValidSubsequence(array, sequence):
    subidx = 0

    for value in array:

        if subidx == len(sequence):
            return True

    if value == sequence[subidx]:


        subidx += 1

    return subidx == len(sequence)