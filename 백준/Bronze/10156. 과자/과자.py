k, n, m = map(int, input().split())

if (k * n) >= m :                 #과자를 사려고 하는 금액(k*n)이 가지고 있는 돈보다 크거나 같을때
  result = (k * n) - m            #부모님께 돈을 받아야 하기때문에 (k*n)-m 값을 할당하여 출력    
else :
  result = 0

print(result)