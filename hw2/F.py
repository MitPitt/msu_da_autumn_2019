def foo(s, l, r, pairs):
    if l == pairs and r == pairs:
        yield(s)
    else:
        if l < pairs:
            for i in foo(s + '(', l + 1, r, pairs):
                yield i
        if r < l:
            for i in foo(s + ')', l, r + 1, pairs):
                yield i
                
def brackets(n):
    for i in foo('',0,0,n):
        yield i

if __name__ == "__main__":
    n = int(input())
    for i in brackets(n):
        print(i)
