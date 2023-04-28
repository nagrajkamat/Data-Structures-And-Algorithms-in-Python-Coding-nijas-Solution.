from sys import stdin

def knapsack(weights, values, n, maxWeight) :
    if (n == 0) or (maxWeight == 0) :
        return 0

    if weights[n - 1] > maxWeight :
        return knapsack(weights, values, n - 1, maxWeight)

    includeItem = values[n - 1] + knapsack(weights, values, n - 1, maxWeight - weights[n - 1])

    excludeItem = knapsack(weights, values, n - 1, maxWeight)

    return max(includeItem, excludeItem)


def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, n, maxWeight))