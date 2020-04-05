import time
import operator
from collections import defaultdict
from collections import OrderedDict


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
    bases = ['A', 'T', 'G', 'C']
    k_list = [*patt]
    for i in range(len(patt)):
        for b in bases:
            if k_list[i] != b:
                tc = k_list[i]
                k_list[i] = b
                k_string = "".join(k_list)
                neighborhood.add(k_string)
                k_list[i] = tc
    return neighborhood


def neighbors_2(patt, d):
    neighborhood = set()
    neighborhood.add(patt)
    res = set()
    for i in range(d):
        while neighborhood:
            nb = neighborhood.pop()
            res.add(nb)
            ins = immediate_neighbors(nb)
            res = res.union(ins)
        neighborhood = res
    return res


def build_neighborhood(kmer, d):
    bases = ['A', 'T', 'G', 'C']
    k_list = [*kmer]
    neighborhood = set()
    neighborhood.add(kmer)
    for i in range(d):
        for k_idx in range(len(k_list)):
            for b in bases:
                if b != k_list[k_idx]:
                    tc = k_list[k_idx]
                    kl_prime = k_list.copy()
                    kl_prime[k_idx] = b
                    k_string = "".join(kl_prime)
                    neighborhood.add(k_string)
    return neighborhood


nb = neighbors_2("AGTCAGTC", 2)
for n in nb:
    if hamming_distance("AGTCAGTC", n) > 2:
        print(n)


def words_with_mismatches(text, k, d):
    kmers = freq_set(text, k)
    mf_dict = defaultdict(int)
    mf_kmers = []
    max_ct = 0
    for km in kmers.keys():
        n_set = neighbors_2(km, d)
        for neighbor in n_set:
            mf_dict[neighbor] += 1
    for km, ct in mf_dict.items():
        if ct > max_ct:
            max_ct = ct
            mf_kmers = [km]
        elif ct == max_ct:
            mf_kmers.append(km)
    print(max_ct)
    return mf_kmers


def print_stuff(xs):
    print(" ".join(str(i) for i in xs))


# def approximate_match(pattern, genome, distance):
#     ps = []
#     last_ham = hamming_distance(genome, pattern[:len(pattern)])
#     for i in range(len(genome[:len(genome) - len(pattern) + 1])):
#         if last_ham <= distance:
#             ps.append(i)
#         inner_ham = last_ham
#         for j in range(0, len(pattern)):
#             if inner_ham > distance:
#                 break
#             else:
#                 inner_ham += hamming_comp(pattern[j], genome(i + j))

file_name = "./course_1/week_2/inputs/mismatch_test.txt"

# with open(file_name) as f:
#     patt = f.readline().strip()
#     indices = f.readline().strip().split(" ")
#     # patt = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
#     # indices = ["4", "1"]
#     k = int(indices[0])
#     d = int(indices[1])
#     print_stuff(words_with_mismatches(patt, k, d))
