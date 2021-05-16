for _ in range(int(input())):
    people,cash = map(int,input().split())
    amount = list(map(int,input().split()))
    for money in amount:
        if money <= cash:
            print(1, end='')
            cash -= money
        else:
            print(0, end='')
    print()
