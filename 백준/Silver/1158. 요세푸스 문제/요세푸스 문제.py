n, k = map(int,input().split())
l = [*range(1, n + 1)]
p = []
i = 0

while l:
 i = (i + k - 1) % len(l)
 p.append(l.pop(i))
 
print('<' + str(p)[1:-1] + '>')