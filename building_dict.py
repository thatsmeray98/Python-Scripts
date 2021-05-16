word = {'B':'BattleShip',
        'C':'Cruiser',
        'D':'Destroyer',
        'F':'Frigate'}
for i in range(int(input())):
    alphabet = input().upper()
    print(word[alphabet])
