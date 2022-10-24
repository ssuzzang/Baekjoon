n = map(int, input().split()) 
    # map 함수 활용해서 type을 지정하고 3개의 요소를 공백기준으로 나눠서 n 변수에 저장

a = sorted(n) # sorted 함수의 디폴트는 오름차순 (작은 수부터)
print(a[1])