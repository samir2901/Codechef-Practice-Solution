t = int(input())
z = []    
for i in range(t):
    x = input().lower()
    if x == 'b':
        z.append('BattleShip')
    elif x == 'c':
        z.append('Cruiser')
    elif x == 'd':
        z.append('Destroyer')
    elif x == 'f':
        z.append('Frigate')
for m in z:
    print(m)
