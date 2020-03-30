import time


def most_frequent(text, k, max=0):
    kmers = {}
    most_frequent_arr = []
    for i in range(0, len(text) - k + 1):
        kmer = text[i:(i + k)]
        count = kmers.get(kmer, 0)
        kmers[kmer] = count + 1
        if kmers.get(kmer, 0) > max:
            max = kmers.get(kmer, 0)
            most_frequent_arr = [kmer]
        elif kmers.get(kmer, 0) == max:
            most_frequent_arr.append(kmer)
    return most_frequent_arr


def clump_finder(text, k, l, t):
    rs = set()
    for i in range(len(text) - l + 1):
        kmers = most_frequent(text[i:i+l], k, t)
        for kmer in kmers:
            rs.add(kmer)
    return " ".join([r for r in rs])


with open("./course_1/inputs/clump_test.txt") as data_set:
    text = data_set.readline().strip()
    ks = data_set.readline().strip()
    input_nums = [int(i) for i in ks.split(" ")]
    k = input_nums[0]
    l = input_nums[1]
    t = input_nums[2]
    t1 = time.time()
    print(clump_finder(text, k, l, t))
    print(time.time() - t1)
