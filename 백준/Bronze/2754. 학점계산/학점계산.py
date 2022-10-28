score = input()
k = 0

if score[0] =='A':
    k += 4
elif score[0] =='B':
    k += 3
elif score[0] =='C':
    k += 2
elif score[0] =='D':
    k += 1

if score =='F':
    k = 0
elif score[1] =='+':
    k += 0.3
elif score[1] =='-':
    k -= 0.3

print(float(k))