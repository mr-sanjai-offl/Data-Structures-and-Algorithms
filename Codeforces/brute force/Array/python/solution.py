n = int(input())
arr = list(map(int,input().split()))

neg = []
pos = []
zero = []

for i in arr:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
    else:
        zero.append(i)

g1 = []
g2 = []
g3 = []

g1.append(neg.pop())

if pos:
    g2.extend(pos)
else:
    g2.append(neg.pop())
    g2.append(neg.pop())

g3.extend(zero)
g3.extend(neg)

print(len(g1), *g1)
print(len(g2), *g2)
print(len(g3), *g3)