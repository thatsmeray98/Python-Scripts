for count in range(int(input())):
    quantity,price = map(int,input().split())
    print('{:6f}'.format(quantity*price - (0.1*quantity*price))) if quantity > 1000 else print('{:6f}'.format(quantity*price))
