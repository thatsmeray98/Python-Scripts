for _ in range(int(input())):
    num = int(input())
    if num%10 == 0:
        print(0)
    elif (num*2)%10 == 0:
        print(1)
    else:
        print(-1)
        