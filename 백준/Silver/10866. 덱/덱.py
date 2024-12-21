from collections import*

a=deque()
f=iter(open(0))
next(f)

for c in f:
 if c[0]=="f":print(a[0]if a else -1)

 elif c[0]=="b":print(a[-1]if a else -1)

 elif c[0]=="s":print(len(a))

 elif c[0]=="e":print(int(len(a)<1))

 elif c[4]=="f":print(a.popleft()if a else -1)

 elif c[4]=="b":print(a.pop()if a else -1)

 elif c[5]=="f":a.appendleft(int(c[11:]))

 else:a.append(int(c[10:]))