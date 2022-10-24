n = int(input())

if n == 1: # 1이 입력될 경우 '' 출력
    print('')
    
for i in range(2, n+1): # 소인수분해로 들어갈 수 있는 모든 경우의 수 반복(2부터 n까지) 
    
    while n % i == 0: # 입력된 n을 i로 나눈 나머지가 0이 될때 까지 반복 
        print(i)
        n = n / i # n 값을 n/i 값으로 갱신 (i가 n보다 크면 갱신된 n은 바로 0이 됨)