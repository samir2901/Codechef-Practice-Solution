t = int(input())
r = []
for x in range(t):
    n = input()
    l = list(n)
    z = list(map(int, l))
    last_digit = z[len(z)-1]
    first_digit = z[0]
    s = last_digit + first_digit
    r.append(s)

for i in r:
    print(i)