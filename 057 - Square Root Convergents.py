import math

def calculateNumerator(i:int):
    if i == 0:
        return 1
    return (2 * calculateDenominator(i-1)) + calculateNumerator(i-1)

def calculateDenominator(i:int):
    if i == 0:
        return 1
    return calculateDenominator(i-1) + calculateNumerator(i-1)


def squareRootConvergents(n:int):
    count = 0
    x = 1
    for i in range(1, n+1):
        n = calculateNumerator(i)
        d = calculateDenominator(i)
        print(i, n, d)
        if int(math.log10(n)) > int(math.log10(d)):
            count += 1
    return count

print(squareRootConvergents(100))