t = int(input())
z = []
for i in range(1,t+1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    s = x + y
    z.append(s)

for i in z:
    print(i)

