n = int(input())
x = 0
for _ in range(n):
    exp = input()
    if exp[1] == &#39;+&#39;:
        x += 1
    else:
        x -= 1
print(x)