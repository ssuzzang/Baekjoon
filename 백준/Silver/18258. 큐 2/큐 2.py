from collections import deque
import sys

r = sys.stdin.readline
p = print
q = deque()
for _ in range(int(r())):
    c = r().split()
    match c[0]:
        case 'push': q.append(c[1])
        case 'pop': p(-1 if not q else q.popleft())
        case 'size': p(len(q))
        case 'empty': p(int(not q))
        case 'front': p(-1 if not q else q[0])
        case 'back': p(-1 if not q else q[-1])