def even(n):
    if n%2==0:
        return True
    else:
        return False

N = int(input())
A = [int(x) for x in input().split()]

l_a = 0
u_a = 0

for i in A:
    if even(i):
        l_a += 1
    else:
        u_a += 1

if l_a > u_a:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
        
