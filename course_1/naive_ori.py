def pattern_count(text, pattern):
    count = 0
    pattern_l = len(pattern)
    for i in range(0, len(text) - pattern_l + 1):
        comp = text[i:(i+pattern_l)]
        print(comp)
        if comp == pattern:
            count += 1
    return count        


with open("./dataset_2_7.txt") as data_set:
    t = data_set.readline()
    p = data_set.readline()
    print(t)
    print(p)
    r = pattern_count(t.strip(), p.strip())
    print(r)
