from collections import defaultdict
import time


def clump_finder_eff(text, k, l, t):
    frequent_kmers = set()
    all_kmers = defaultdict(int)
    for i in range(l - k + 1):
        kmer = text[i:i+k]
        all_kmers[kmer] += 1
        if all_kmers[kmer] >= t:
            frequent_kmers.add(kmer)
    first_kmer = text[:k]
    first_kmer_idx = 0
    for i in range(l - k, len(text) - k + 1):
        all_kmers[first_kmer] -= 1
        first_kmer_idx += 1
        first_kmer = text[first_kmer_idx:first_kmer_idx+k]
        curr_kmer = text[i:i+k]
        all_kmers[curr_kmer] += 1
        if all_kmers[curr_kmer] >= t:
            frequent_kmers.add(curr_kmer)
    return frequent_kmers


with open("./course_1/inputs/E_coli.txt") as data_set:
    text = data_set.readline().strip()
    ks = data_set.readline().strip()
    # input_nums = [int(i) for i in ks.split(" ")]
    # k = input_nums[0]
    # l = input_nums[1]
    # t = input_nums[2]
    t1 = time.time()
    res = clump_finder_eff(text, 9, 500, 3)
    print(time.time() - t1)
    print(len(res))
