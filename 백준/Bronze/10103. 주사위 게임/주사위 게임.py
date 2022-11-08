n = int(input())
ares, bres = 100, 100
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        bres -= a
    elif a < b:
        ares -= b
print(ares, bres, sep='\n')