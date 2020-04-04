import time
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

file_name = "./week_2/inputs/dataset_9_6.txt"
with open(file_name) as f:
    patt = f.readline().strip()
    gene = f.readline().strip()
    dist = f.readline().strip()
    t1 = time.time() 
    xs = approx_naive(patt, gene, int(dist))
    print(time.time() - t1)
    print(len(xs))