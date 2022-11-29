t = int(input())
for i in range(t):
    total = 0   # 평점
    c_tot = 0   # 총 학점
    t = 0
    n = int(input())
    for j in range(n):
        c, g = map(float, input().split())
        c_tot += c
        t += c * g
    total = t / c_tot
    print(int(c_tot), '%.1f' %total)