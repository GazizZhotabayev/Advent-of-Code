from collections import Counter
f = lambda x: Counter(x).most_common()
print(f('1100'))