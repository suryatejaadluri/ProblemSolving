def nonConstructibleChange(coins):
    # Write your code here. - O(nlogn)
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        else:
            currentChange += coin
    return currentChange + 1