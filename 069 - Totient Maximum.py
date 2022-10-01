
def phi(n:int):
    count = n-1
    divisors = []
    for i in range(2, n-1):
        #print("i =", i)
        fail = False
        for div in divisors:
            if i % div == 0:
                count -= 1
                fail = True
                break
        if fail: continue
        if n % i == 0:
            count -= 1
            divisors.append(i)
    return count

#this actually takes over 2 hours to run
def solution(n:int):
    maxx = 0
    maxn = 0
    for i in range(n, 1, -1):
        x = i / phi(i)
        if x > maxx:
            maxx = x
            maxn = i
    return maxn

print(solution(1000000))