for i in range(int(input())):
    turn,num = map(int,input().split())
    for count in range(turn):
        #num = int((num*(num+1))/2)
        num = (num*(num+1))//2
    print(num)