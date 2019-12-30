t = int(input())
z = []
for i in range(t):
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        z.append('>')
    elif x < y:
        z.append('<')
    elif x==y:
        z.append('=')

for c in z:
    print(c)