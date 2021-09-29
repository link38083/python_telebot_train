from collections import Counter

def find_uniq(arr):
  return Counter(arr).most_common()[1][0]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))