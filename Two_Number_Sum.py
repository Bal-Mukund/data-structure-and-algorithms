""" [Question]  Write a function that takes in a non-empty array of distinct integers and 
                an integer representing a target sum. If any two numbers in the input array 
                sum up to the target sum, the function should return them in an array, in any order.
                If no two numbers sum up to the target sum, the function should return an empty array. """



def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum ]
    return []
