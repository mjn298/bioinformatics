def pattern_count(text, pattern):
    count = 0
    indices = []
    pattern_l = len(pattern)
    for i in range(0, len(text) - pattern_l + 1):
        comp = text[i:(i+pattern_l)]
        if comp == pattern:
            indices.append(i)
    return indices
