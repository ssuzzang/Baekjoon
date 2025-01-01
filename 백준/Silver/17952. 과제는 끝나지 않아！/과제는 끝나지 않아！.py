import sys

n = int(sys.stdin.readline())

stack, score = [], 0 

for _ in range(n):
    homework = list(map(int, sys.stdin.readline().split())) 
    if homework[0] == 1:
        if homework[2]-1 == 0: 
            score += homework[1]
        else: 
            stack.append([homework[1], homework[2]-1])
    elif stack: 
        stack[-1][1] -= 1
        if stack[-1][1] == 0: 
            score += stack[-1][0]
            stack.pop()
            
print(score)