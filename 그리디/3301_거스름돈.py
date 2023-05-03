n = int(input())

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = 0

for i in change:
    cnt += n // i
    n = n % i
    
print(cnt)

