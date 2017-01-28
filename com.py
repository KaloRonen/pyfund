from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


def gen123():
    print("About to yield 1")
    yield 1
    print("About to yield 2")
    yield 2
    print("About to yield 3")
    yield 3
    print("About to return")


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b
