t = int(input())
x = [100,50,10,5,2,1]
z = []
for i in range(t):
    r = int(input())
    c = 0
    for j in x:
        b = r//j
        c += b
        r %= j
    z.append(c)

for a in z:
    print(a)


