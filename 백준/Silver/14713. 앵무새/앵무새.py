import sys

n=int(sys.stdin.readline())
arr=[]

length=0

for i in range(n):
    arr.append(sys.stdin.readline().split())
    length+=len(arr[i])
    arr[i].append(0)

res=sys.stdin.readline().split()

for word in res:
    isOk=0 
    for i in range(n):
        if arr[i][0]==word:
            arr[i].pop(0)
            isOk=1
            break
    if isOk==0:
        break

if isOk==0 or length!=len(res):
    print("Impossible")
elif isOk==1 and length==len(res):
    print("Possible")