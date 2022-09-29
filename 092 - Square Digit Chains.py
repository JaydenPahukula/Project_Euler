

def squareDigitChains1(N:int):

    bigList = [0] * N
    bigList[1] = 1
    bigList[89] = 89
    
    for i in range(1, N):

        
        if bigList[i] == 0:
            x = i
            cache = [x]
            while 1:

                if bigList[x] == 1:
                    for item in cache:
                        bigList[item] = 1
                    break
                if bigList[x] == 89:
                    for item in cache:
                        bigList[item] = 89
                    break

                cache.append(x)

                temp = 0
                for c in str(x):
                    temp += int(c)**2
                x = temp

    #final count
    count = 0     
    for item in bigList:
        if item == 89:
            count += 1

    return count

#init
N = 10000000
parent = [0] * (N)
for i in range(N):
    parent[i] = i

def find(n:int):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(x, y):
    parent[find(y)] = find(x)
    return

def squareDigitChains():

    #set all parents
    for i in range(N):
        temp = 0
        for c in str(i):
            temp += int(c)**2
        parent[i] = temp
    parent[1] = 1
    parent[89] = 89
    
    #count all roots
    count = 0
    for i in range(N):
        if find(i) == 89:
            count += 1

    return count

print(squareDigitChains())