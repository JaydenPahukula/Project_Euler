import math
import mpmath as mp
from decimal import *

mp.dps = 20

def checkPatterns(a):
    possiblePatterns = []
    for i in range(2, len(a)):
        print("\n\ni =", i)
        print("a =", a[:i])
        #test patterns
        for pattern in possiblePatterns:
            if len(possiblePatterns) == 0 or k >= len(possiblePatterns):
                break
            print("checking", possiblePatterns[k])
            fail = False
            for j in range(1,i):
                if a[j] != possiblePatterns[k][1][j % len(possiblePatterns[k][1]) - 1]:
                    fail = True
                    print("failed")
                    break
            if fail:
                continue
            else:
                possiblePatterns[k][2] += 1
                k += 1
                print("success")

        #check for new patterns
        if a[i-1] == a[1]:
            possiblePatterns.append([0, a[1:i]])
        
        print("patterns =", possiblePatterns)
        input()

    return possiblePatterns[0][1]


def sequence(n):
    #the amount of times a pattern needs to repeat to be confirmed
    REQUIREMENT = 10
    a = [0]
    a[0] = math.floor(math.sqrt(n))
    x = a[0]
    numer = 1
    i = 1
    patterns = []
    while 1:

        #calculate a[i]
        denom = (n - x**2) / numer
        group = (x + math.sqrt(n)) / denom
        a.append(0)
        a[i] = math.floor(group)
        x = abs(x - (denom*a[i]))
        numer = denom


        #check patterns
        for pattern in patterns:
            if pattern[1] == -1:
                continue
            if a[i] == pattern[0][(i-1) % len(pattern[0])]:
                pattern[1] += 1
                if pattern[1] == REQUIREMENT:
                    return [a[0], pattern[0]]
            else:
                pattern[1] = -1

        #look for new patterns
        #print("looking for new patterns...")
        if a[i] == a[1]:
            if i == 1:
                patterns.append([[a[1]], 0])
            else:
                patterns.append([a[1:i], 0])

        #print("patterns =", patterns)
        #print(len(a))
        if len(a) > 1000:
            print(a)
            input()
        #input()
        i += 1

    return a

def oddPeriodSquareRoots(N):
    count = 0
    for num in range(2, N+1):
        #skip square numbers
        if math.sqrt(num) % 1 == 0:
            continue

        pattern = sequence(num)[1]
        print("\n", num, "-", pattern, "\n period =", len(pattern))
        if len(pattern) % 2 == 1:
            count += 1
            print("^odd ------\n")
        else:
            print("-----------\n")
    return count

print(oddPeriodSquareRoots(10000))

#tried:
#152