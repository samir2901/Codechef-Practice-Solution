from math import *

r = int(input()) #no. of rounds
s1 = [] #scores of player one
s2 = [] #scores of player two
for a in range(r):
    x, y = input().split()
    x = int(x)
    y = int(y)
    s1.append(x)
    s2.append(y)

l = []

for i,j in zip(s1,s2):
    x = i - j
    l.append(x)

l.sort()
if abs(l[0]) > abs(l[len(l)-1]):
    print(2,abs(l[0]))
else:
    print(1,abs(l[len(l)-1]))


    

    




