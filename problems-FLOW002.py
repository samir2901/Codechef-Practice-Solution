t = int(input())
z = []
for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    z.append(a%b)

print(*z,sep="\n")