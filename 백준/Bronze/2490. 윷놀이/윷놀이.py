arr = ['D', 'C', 'B', 'A', 'E']
for _ in range(3):
    total = sum(map(int, input().split()))
    print(arr[total])