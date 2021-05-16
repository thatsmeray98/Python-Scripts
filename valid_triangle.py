for i in range(int(input())):
    x,y,z = map(int,input().split())
    print('YES') if x+y+z == 180 else print('NO')
    