N = int(input())
apple = 0
for i in range(N):
    A, B = map(int, input().split())
    apple += B % A
    
print(apple)