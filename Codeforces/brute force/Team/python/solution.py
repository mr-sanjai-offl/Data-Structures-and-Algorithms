n = int(input())
ans = 0
for _ in range(n):
    prob = list(map(int,input().split()))
    if prob.count(1) > prob.count(0):
        ans += 1
print(ans)