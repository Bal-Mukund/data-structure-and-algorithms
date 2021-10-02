def sortedSquaredArray(array):
    sqd = []

    for value in array:
        sqd.append(value * value)

    return sorted(sqd)