def isPrime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    else:       
        return True

t = int(input())
z = []
for i in range(t):
    x = int(input())
    if isPrime(x):
        z.append('yes')
    else:
        z.append('no')

for m in z:
    print(m)
    