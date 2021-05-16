for i in range(int(input())):
    coins, people = map(int,input().split())
    maximum = 0
    for count in range(1, people+1):
        if maximum < (coins%count):
            maximum = coins % count
    print(maximum)
