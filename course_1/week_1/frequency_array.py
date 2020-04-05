def pattern_to_number(pattern):
    vals = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    sum = 0
    for i in range(len(pattern)):
        sum += vals[pattern[i]] * (4 ** (len(pattern) - i - 1))
    return sum


def get_n(i):
    return{
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }[i]


def number_to_pattern(n, k):
    p = []
    while(k > 0):
        mod = n % 4
        flr = n // 4
        p.append(get_n(mod))
        k -= 1
        n = flr
    return ''.join(reversed(p))


def list_get(l, idx):
    try:
        return l[idx] if l[idx] is not None else 0
    except IndexError:
        return 0


def computing_frequencies(t, k):
    freq_arr = [0] * (4 ** k)
    for i in range(0, len(t) - k + 1):
        p = t[i:i+k]
        j = pattern_to_number(p)
        freq_arr[j] = freq_arr[j] + 1
    return freq_arr
