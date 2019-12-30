t = int(input())
z = []
for i in range(t):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b+c == 180:
        z.append('YES')
    else:
        z.append('NO')

for j in z:
    print(j)