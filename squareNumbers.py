__author__ = 'chisaton'


def square(x):
    return x*x

# print(square(3))


def log2(x):
    if x == 2:
        return 1
    return 1 + log2(x/2)

print(log2(16))
