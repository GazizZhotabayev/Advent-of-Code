from itertools import permutations
import time
from random import randint

#30 random yoghurt densities
yoghurt_densities = [randint(1,100) for i in range(30)]

#list of indices: 0,1,2,3,...,29 that we will be permuting 
indices = list(range(30))

#acceptable range()

t0 = time.time()

top = 0
for p in permutations(indices, 10):
    

t1 = time.time()
print(f'Done: it took {t1-t0} seconds, or {(t1-t0)/60} minutes')

print(f"Here's our list of yoghurt densities: /n{yoghurt_densities}")
print(f"And here's the ")