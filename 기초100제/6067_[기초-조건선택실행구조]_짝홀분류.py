"""
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
"""

n = int(input())

if n < 0:
    print("A" if not n % 2 else "B")
    
else:
    print("C" if not n % 2 else "D")
