import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **argv):
        if wrapper.tempdepth == 0:
            wrapper.rdepth = 0
            wrapper.ncalls = 0
        wrapper.tempdepth +=1
        wrapper.ncalls +=1
        result = func(*args, **argv)
        if wrapper.tempdepth > wrapper.rdepth:
            wrapper.rdepth = wrapper.tempdepth
        wrapper.tempdepth -=1
        return result
    wrapper.tempdepth = 0
    wrapper.rdepth = 0
    wrapper.ncalls = 0
    return wrapper


@counter
def func2(n, steps):
    if steps == 0:
        return

    func2(n + 1, steps - 1)
    func2(n - 1, steps - 1)

if __name__ == "__main__":
    func2(0, 5)
    print(func2.ncalls, func2.rdepth)

    func2(0, 3)
    print(func2.ncalls, func2.rdepth)


