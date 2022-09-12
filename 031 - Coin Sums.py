coins = [100,50,20,10,5,2,1]
target = 200


def findPermutations(t=0, n=0):
    ways = 0
    for i in range(target,t-1,-coins[n]):
        if t + i < target:
            ways += findPermutations(t + i, n+1)
    return ways


print(findPermutations())
