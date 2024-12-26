from collections import deque
n = int(input())
inp = list(map(int, input().split()))
dq = deque([])
inp.reverse()
for i in range(n):
    if inp[i] == 1:
        dq.appendleft(i+1)
    elif inp[i] == 2:
        a = dq.popleft()
        dq.appendleft(i+1)
        dq.appendleft(a)
    elif inp[i] == 3:
        dq.append(i+1)
for i in dq:
    print(i,end=" ")