def smallestDifference(arrayOne, arrayTwo):
  # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    p1 = 0
    p2 = 0
    bestnum = [arrayOne[0],arrayOne[1]]
    end1 = len(arrayOne) - 1
    end2 = len(arrayTwo) - 1
    Minabsdiff = abs(arrayTwo[0] - arrayOne[0])
    while p1 <= end1 and p2 <= end2:
        num2 = arrayTwo[p2]
        num1 = arrayOne[p1]
        diff = abs(num2 - num1)
        if diff < Minabsdiff:
            Minabsdiff = diff
            bestnum = [num1,num2]
            print(bestnum)
        if num1 < num2:
            p1 += 1
        elif num1 > num2:
            p2 += 1
        else:
            return [num1,num2]
    return bestnum