a, b = map(int, input().split())
c = format(a/b, ".2f")

print(f"{a + b}\n{a - b}\n{a * b}\n{a // b}\n{a % b}\n{c}")
