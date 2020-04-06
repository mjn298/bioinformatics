import time


def calc_skew(n, skew):
    if n == 'G':
        return skew + 1
    elif n == 'C':
        return skew - 1
    else:
        return skew


def skew(genome):
    length = len(genome)
    s = 0
    ss = [0]
    for i in range(length):
        n = genome[i]
        s = calc_skew(n, s)
        ss.append(s)
    return ss


def min_skew(genome):
    length = len(genome)
    s = 0
    min = 0
    mins = []
    for i in range(length):
        n = genome[i]
        s = calc_skew(n, s)
        if s == min:
            mins.append(i + 1)
        elif s < min:
            min = s
            mins = [i + 1]
    return mins

def print_stuff(xs):
    print(" ".join(str(i) for i in xs))
