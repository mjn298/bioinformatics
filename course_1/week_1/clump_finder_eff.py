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
