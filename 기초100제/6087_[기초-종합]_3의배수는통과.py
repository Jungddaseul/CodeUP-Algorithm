﻿n = int(input())

for k in range(1, n+1):
    if k % 3 == 0:
        continue
    print(k, end=' ')
