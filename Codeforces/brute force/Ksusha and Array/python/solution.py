n = int(input())
arr = list(map(int,input().split()))

m = min(arr)

res = m
for i in arr:
    if i % m != 0:
        res = -1
        break
    
print(res)    