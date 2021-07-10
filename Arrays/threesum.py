def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for idx,num1 in enumerate(array):
        left = idx+1
        right = len(array)-1
        while left<right:
            currentSum = num1 + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([num1,array[left],array[right]])
                left += 1
                right -= 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
    return triplets