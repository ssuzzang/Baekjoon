t = int(input())
for i in range(t):
    t = 0
    price = int(input())
    option = int(input())
    for j in range(option):
        a, b = map(int, input().split())
        t += a * b
    print(price + t)