def product(a):
    result = [[]]
    for i in a:
        result = [x+[y] for x in result for y in i]
    for prod in result:
        yield tuple(prod)

if __name__ == "__main__":
    a = [[0, 1], [2, 3], [4]]
    for e in product(a):
        print(e)
    a = [[0, 1], 'python']
    for e in product(a):
       print(e)
