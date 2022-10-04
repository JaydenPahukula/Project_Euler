
knowns = {}

def solution(n:int, list=[]):
    ways = 0

    if list == []: last = 1
    else: last = list[-1]

    #check if already known
    situation = (last * 1000000) + n - sum(list)
    if last > 1 and situation in knowns:
        return knowns[situation]

    #calculate number of ways
    templist = list.copy()
    templist.append(0)
    listlen = len(list)
    for x in range(last, n):
        templist[listlen] = x
        s = sum(templist)
        if s == n: #success
            ways += 1
            break
        elif s > n: #busted
            break
        else: #go another layer deeper
            ways += solution(n, templist)

    #add situation to list on knowns
    if last > 1:
        knowns[situation] = ways

    return ways

print(solution(100))