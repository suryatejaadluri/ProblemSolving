def fourNumberSum(array, targetSum):
    # Write your code here.
    result = []
    Hashtable = {}
    for i in range(len(array)):
        j=i+1
        while j<len(array):
            two_sum = array[i]+array[j]
            if two_sum in Hashtable:
                Hashtable[two_sum].append([array[i],array[j]])
            else:
                Hashtable[two_sum] = [[array[i],array[j]]]
            j+=1
    for key in Hashtable:
        requiredSum = targetSum - int(key)
        if requiredSum in Hashtable:
            for values in Hashtable[requiredSum]:
                for two_sums in Hashtable[key]:
                    first,second = values
                    third,fourth = two_sums
                    if first == third or first == fourth or second == third or second==fourth:
                        continue
                    quad = sorted([first,second,third,fourth])
                    if quad not in result:
                        result.append(quad)
    return result
array = [1, 2, 3, 4, 5, 6, 7]
targetSum = 10
print(fourNumberSum(array,targetSum))

