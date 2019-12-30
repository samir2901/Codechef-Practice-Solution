def ispalindrome(n):
    x = n[::-1]
    if n == x:
        return True
    else:
        return False

t = int(input())
l = []
for i in range(t):
    z = input()
    if ispalindrome(z):
        l.append('wins')
    else:
        l.append('losses')

for j in l:
    print(j)
    


