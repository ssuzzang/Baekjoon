n = int(input())
X = [0,1]
while(len(X) < n+1):
    X.append(X[-1]+X[-2])
print(X[-1])