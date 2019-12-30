t = int(input())
l = []
for i in range(t):
    x = input()
    x = x[::-1]
    l.append(int(x))
for i in l:
    print(i)

