n, k = map(int,input().split())
scr = list(map(int,input().split()))
 
k_scr = scr[k-1]
cnt = 0
 
for i in scr:
    if i >= k_scr and i != 0:
        cnt += 1
 
print(cnt)