pasta = []
juice = []

for i in range(3):
    pasta.append(int(input()))
    
for i in range(2):
    juice.append(int(input()))
    
min_price = pasta[0] + juice[0]

for i in pasta:
    for j in juice:
        if i + j < min_price:
            min_price = i + j

print("%.1f" %(min_price*1.1))

    
