N = int(input())
A = list(map(int, input().split()))
S = 0 

for i in A: 
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        S += 1
print(S)