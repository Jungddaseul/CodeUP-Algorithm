"""
# 문제풀이 1

a = list(input())

for i in range(0, len(a), 2):
    print(a[i]+a[i+1], end=" ")
"""

# 문제풀이 2

a = input()
print(a[0:2], a[2:4], a[4:])
