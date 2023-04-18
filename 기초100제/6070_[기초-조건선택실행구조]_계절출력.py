"""
월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""

n = int(input())

if 3 <= n <= 5:
    print("spring")

elif 6 <= n <= 8:
    print("summer")

elif 9 <= n <= 11:
    print("fall")

elif n == 12 or n == 1 or n == 2:
    print("winter")
