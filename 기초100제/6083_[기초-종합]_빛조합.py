from itertools import product

r, g, b = map(int, input().split())
arr = [list(range(r)), list(range(g)), list(range(b))]
comb = list(product(*arr))

for k in comb:
    print(k[0], k[1], k[2])
print(len(comb))
