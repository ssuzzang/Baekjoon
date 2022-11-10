t = int(input())

for _ in range(t) :
  n = int(input())
  data = list(input().split())
  
  for _ in range(n - 1) :
    a, b = input().split()
    if int(data[1]) < int(b) :
      data[0] = a
      data[1] = b
  
  print(data[0])