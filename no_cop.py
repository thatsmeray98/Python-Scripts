'''
house_num = [1 for i in range(1,101)]
for _ in range(int(input())):
    m,x,y = map(int,input().split())
    cop_house = sorted(list(map(int,input().split())))
    for house in cop_house:
        lower = house - x*y
        upper = house + x*y
        if lower < 1:
            lower = 1
        if upper > 100:
            upper = 100
        for num in range(lower,upper+1):
            print(num)
            #house_num[num] = 0
    print(house_num.count(1))
''' 
'''
for i in range(int(input())):
    houses = [1 for _ in range(100)]
    m,x,y = map(int,input().split())
    cops = sorted(list(map(int,input().split())))
    for num in cops:
        upper = num + x*y
        lower = num - x*y
        if lower < 1:
            lower = 1
        if upper > 100:
            upper = 100
        for num in range(lower,upper+1):
            if houses[num-1] == 1:
                houses[num-1] = 0
    print(houses.count(1))
'''
for i in range(int(input())):
    #houses = [1 for _ in range(100)]
    m, x, y = map(int, input().split())
    cops = sorted(list(map(int, input().split())))
    for num in cops:
        upper = num + x*y
        lower = num - x*y
        if lower < 1:
            lower = 1
        if upper > 100:
            upper = 100
        for num in range(lower, upper+1):
            if num not in cops:
                cops.append(num)
    print(cops,len(cops),100-len(cops))
