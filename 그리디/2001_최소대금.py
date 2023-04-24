pasta = []
juice = []

# 파스타 가격입력
for i in range(3):
    pasta.append(int(input()))

# 주스 가격입력
for i in range(2):
    juice.append(int(input()))

# 임의의 최소대금설정
min_price = pasta[0] + juice[0]

# 최소대금 비교
for i in pasta:
    for j in juice:
        if i + j < min_price:
            min_price = i + j

print("%.1f" %(min_price*1.1))
