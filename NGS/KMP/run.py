from functions import *

pattern = 'ATAGTGCAT'
file = 'pattern_search_dataset.txt'
# print(compute_prefix_table('ababbaba'))
# occurences = naive_matcher(file, pattern)
# print(occurences)

bestp = compute_prefix_table(pattern)
print(bestp)

print(kmp_matcher(file, pattern))