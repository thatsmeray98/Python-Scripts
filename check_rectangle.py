for _ in range(int(input())):
    x,y,z,w = map(int, input().split())
    print('YES') if (x==y and z==w) or (x==w and y==z) or (y==w and x==z) else print('NO')
