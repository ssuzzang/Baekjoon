n = list(map(int, input().split()))
a = 0
for i in n:
    a += i*i
 
print(a % 10)