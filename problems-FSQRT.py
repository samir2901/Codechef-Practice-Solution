from math import sqrt
T = int(input())
l = []
for i in range(T):
    x = int(input())
    l.append(int(sqrt(x)))
for i in l:
    print(i)