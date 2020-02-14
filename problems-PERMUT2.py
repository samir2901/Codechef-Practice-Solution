t = int(input())
z = []
while t != 0:
    seq = [int(x) for x in input().split()]
    inv = [None]*t
    for i in range(t):
        inv[seq[i]-1] = i+1
    if inv != seq:
        z.append('not ambiguous')
    else:
        z.append('ambiguous')
    t = int(input())
for m in z:
    print(m)
    



