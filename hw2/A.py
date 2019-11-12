def solution1(word):
    return [i*4 for i in word]

def solution2(word):
    return [word[i]*(i+1) for i in range(len(word))]

def solution3(a):
    return [i for i in a if (i%5==0 or i%3==0)]

def solution4(arr):
    return [j for i in arr for j in i]

def solution5(n):
    return [(a,b,c) for c in range(1,n+1)
            for b in range(1,c+1)
            for a in range(1,b+1)
            if (a**2 + b**2 == c**2)]

def solution6(a):
    return [[i+j for j in a[1]] for i in a[0]]

def solution7(matr):
    return [list(i) for i in zip(*matr)]

def solution8(arr):
    return [[j for j in map(int, i.split())] for i in arr]

def solution9(a):
    return {chr(ord('a')+i):i**2 for i in a}

def solution10(arr):
    return {i.capitalize() for i in arr if len(i)>3}

solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}



if __name__ == "__main__":
    print(solution1('python'))
    print(solution2('python'))
    print(solution3(range(16)))
    print(solution4([[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]]))
    print(solution5(15))
    print(solution6(([0, 1, 2], [0, 1, 2, 3, 4])))
    print(solution7([[1, 2], [3, 4], [5, 6]]))
    print(solution7([[1, 3, 5], [2, 4, 6]]))
    print(solution8(["0", "1 2 3", "4 5 6 7", "8 9"]))
    print(solution9(range(0, 7)))
    print(solution10(['Alice', 'vova', 'ANTON', 'Bob',
                      'kAMILA', 'CJ', 'ALICE', 'Nastya']))
