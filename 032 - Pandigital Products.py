
def permute(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    l = []
    for i in range(len(array)):
        n = array[i]
        array2 = array[:i] + array[i+1:]
        for p in permute(array2):
           l.append([n] + p)
    return l

permutations = permute([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("found all permutations of 1-9")




for p in range(len(permutations)):
    for i in range(5):
        sa = ""
        for a in range(i):
            sa += str(permutations[p][a])
        for j in range(i, 8):
            sb = 1
            for b in range(j):
                continue

    break





def isPandigital(a:int, b:int):
    c = a * b
    s = str(a) + str(b) + str(c)
    print(s)
    if len(s) == 9:
        print(s)
    return

