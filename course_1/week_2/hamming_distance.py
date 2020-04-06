from collections import defaultdict
from course_1.week_1 import reverse_complement


def freq_set(text, k):
    kmers = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        kmer = text[i:(i + k)]
        kmers[kmer] += 1
    return kmers


def hamming_distance(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d


def hamming_comp(c1, c2):
    if c1 != c2:
        return 1
    else:
        return 0


def approx_naive(pattern, genome, distance):
    ps = []
    for i in range(len(genome[:len(genome) - len(pattern) + 1])):
        if hamming_distance(pattern, genome[i:i+len(pattern)]) <= distance:
            ps.append(i)
    return ps


def immediate_neighbors(patt):
    neighborhood = set()
    neighborhood.add(patt)
    bases = ['A', 'T', 'G', 'C']
    for i in range(len(patt)):
        for b in bases:
            k_list = [*patt]
            if k_list[i] != b:
                k_list[i] = b
                k_string = "".join(k_list)
                neighborhood.add(k_string)
    return neighborhood


def neighbors_2(patt, d):
    neighborhood = set()
    neighborhood.add(patt)
    res = set()
    for i in range(d):
        inner_set = res.copy()
        while neighborhood:
            nb = neighborhood.pop()
            ins = immediate_neighbors(nb)
            for n in ins:
                res.add(n)
        neighborhood = res.difference(inner_set)
    return res


def neighbors_rec(pattern, d):

    if d == 0:
        return [pattern]  # It is important to return a list, not just a text

    if len(pattern) == 1:
        return ["A", "C", "G", "T"]

    neighborhood = set()
    suffix = pattern[1:]
    suffix_neighbors = neighbors_rec(suffix, d)

    for string in suffix_neighbors:
        if hamming_distance(string, suffix) < d:
            for symbol in ["A", "C", "G", "T"]:
                neighborhood.add(symbol + string)
        else:
            neighborhood.add(pattern[0] + string)

    return neighborhood


def words_with_mismatches(text, k, d, rc=False):
    freq_array = defaultdict(int)
    n = len(text)
    for i in range(n - k + 1):
        patt = text[i:i + k]
        nbs = neighbors_2(patt, d)
        for p in nbs:
            freq_array[p] += 1
        if rc:
            rev = reverse_complement.get_complement(patt)
            rns = neighbors_2(rev, d)
            for rn in rns:
                freq_array[rn] += 1

    max_ct = max(freq_array.values())
    print(max_ct)
    return sorted([k for k, v in freq_array.items() if v >= max_ct])


def print_stuff(xs):
    print(" ".join(str(i) for i in xs))


file_name = "./inputs/dataset_9_8.txt"

with open(file_name) as f:
    patt = f.readline().strip()
    indices = f.readline().strip().split(" ")
    # patt = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    # indices = ["4", "1"]
    k = int(indices[0])
    d = int(indices[1])
    thing = words_with_mismatches(patt, k, d, True)
    print(" ".join(thing))
