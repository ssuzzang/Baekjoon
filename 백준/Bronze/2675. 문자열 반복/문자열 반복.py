t = int(input())
for i in range(t):
    num, s = input().split()   # split공백기준으로 입력 값 분리
    text = ''
    for i in s:
        text += int(num) * i   #반복횟수에 문자열 곱해서 출력
    print(text)