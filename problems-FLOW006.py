def sum_digits(n):
    s = 0
    while n != 0:
        rem = n%10
        s += rem
        n //= 10
    return s

z =[]

t = int(input())
for i in range(t):
    x = int(input())
    z.append(sum_digits(x))

for m in z:
    print(m)
