import itertools
import math


def factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def to_factor_list(n):
    # A factor list is a list of zero or more factors
    # A factor is a number with optional factor list
    fl = []
    for k, group in itertools.groupby(sorted(factor(n))):
        length = sum(1 for _ in group)
        fl.append([k, *to_factor_list(length)])
    return fl


def from_factor_list(factor_list):
    result = 1
    for factor, *fl in factor_list:
        result *= factor ** from_factor_list(fl)

    return result


if __name__ == '__main__':
    import sys

    for a in [int(a) for a in sys.argv[1:]] or range(1, 1001):
        print(a, '->', to_factor_list(a))
