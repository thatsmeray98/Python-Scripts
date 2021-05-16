items = [2**(i-1) for i in range(1,13)]
for i in range(int(input())):
    price = int(input())
    order,count = 0,0
    if price not in items:
        restart = True
        while restart:
            for item in sorted(items,reverse = True):
                if order+item <= price:
                    order += item
                    count += 1 
                    restart = True
                    break
                restart = False
        print(count)
    else:
        print(1)
