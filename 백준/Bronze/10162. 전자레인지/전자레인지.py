t = int(input())

time = [300, 60, 10]
ans = []
cnt = 0
if t%10 != 0: # 10으로 나누어 떨어지면 -1
    print(-1)
else:
    for i in time:  # 전자렌지 작동 횟수
        cnt = t//i
        ans.append(cnt)
        t%=i
    print(ans[0], ans[1], ans[2], sep=' ')
    
