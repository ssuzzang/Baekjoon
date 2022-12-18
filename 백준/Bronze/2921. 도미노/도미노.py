N = int(input())
res = 0
for i in range(0, N+1):
    for j in range(0, i+1):
        res += (i+j)
print(res)