n = int(input())
for i in range(n, 0, -1):
    a = (' '*(n-i) + '*'*(2*i-1))
    print(a)