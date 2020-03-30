def get_other_side(n):
  return {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
  }[n]

def get_complement(text):
  return ''.join([get_other_side(text[i]) for i in range(len(text) - 1, -1, -1)])


print(get_complement("AAAACCCGGT"))

with open("./course_1/dataset_3_2.txt") as data_set:
  ds = data_set.readline().strip()
  print(get_complement(ds))
