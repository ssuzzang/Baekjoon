T = int(input())

for i in range(T) :
    case = list(map(str,input().split())) #특수문자 때문에 str
    res = float(case[0])                  #첫글자는 숫자기때문에 float
    for y in range(len(case)) :   
        if case[y] == '@' :
            res *= 3
        elif case[y] == '%' :
            res += 5
        elif case[y] == '#' :
            res -= 7
    print("%0.2f" % res)                 #소수2자리