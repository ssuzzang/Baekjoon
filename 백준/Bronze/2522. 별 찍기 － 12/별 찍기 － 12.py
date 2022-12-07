N = int(input())
for i in range(1, N+1):
    a = (' '*(N-i) + '*'*i)
    print(a)
for i in range(1, N):
    a = (' '*(i) + '*'*(N-i))
    print(a)