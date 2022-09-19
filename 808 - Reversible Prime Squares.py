
#checks if input is a palindrome
def isPalindrome(input):
    n = str(input)
    for i in range(round(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True

#finds all primes below n
def findPrimes(n:int):
    primes = []
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i*i,n,i):
                nums[j] = False
    return primes
    if num <= 1:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

#returns an int with its digits reversed (123 -> 321)
def reverse(num:int):
    string = str(num)
    reverseString = ''
    for c in string:
        reverseString = c + reverseString
    return int(reverseString)


def reversiblePrimeSquares(n:int):
    primes = findPrimes(100000000)
    print("found primes")
    p = 0
    while 1:
        primes[p] = primes[p] ** 2
        if isPalindrome(primes[p]):
            primes.pop(p)
        else:
            p += 1
            if p >= len(primes):
                break
    print("found primes")
    RPSs = []
    while 1:
        r = reverse(primes[0])
        if r in primes:
            RPSs.append(primes[0])
            RPSs.append(r)
            print(len(RPSs))
            if len(RPSs) >= n:
                return RPSs
            primes.remove(r)
        primes.pop(0)
    return

print(reversiblePrimeSquares(10))
