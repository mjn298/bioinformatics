def get_other_side(n):
    return {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }[n]


def get_complement(text):
    return ''.join([get_other_side(text[i]) for i in range(len(text) - 1, -1, -1)])
