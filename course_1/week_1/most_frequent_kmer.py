def most_frequent(text, k):
    kmers = {}
    max = 0
    for i in range(0, len(text) - k + 1):
        kmer = text[i:(i + k)]
        count = kmers.get(kmer, 0)
        kmers[kmer] = count + 1
        if kmers.get(kmer, 0) > max:
            max = kmers.get(kmer, 0)
    return [k for k, v in kmers.items() if v >= max]
