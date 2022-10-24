# 숫자 2개와 그 사이에 * 혹은 +를 입력받는다 
a = int(input())
b = input()
c = int(input())

if b == "*": # b가 * 라면 곱해주고 아니면 + 해준다
    print(a*c)
else:
    print(a+c)