for i in range(int(input())):
    x,y = map(int,input().split())
    if x>y:
        print('>')
    elif x<y:
        print('<')
    else:
        print('=')