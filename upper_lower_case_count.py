for _ in range(int(input())):
    n,k = map(int,input().split())
    message = input()
    small, large = 0, 0
    for i in message:
        if i>='a' and i<='z':
            small+=1
        elif i>='A' and i<='Z':
            large+=1
    if small>k and large>k:
        print('none')
    elif small>k:
        print('brother')
    elif large>k:
        print('chef')
    else:
        print('both')