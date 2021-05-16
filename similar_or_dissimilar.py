for _ in range(int(input())):
    dish1 = input().split()
    dish2 = input().split()
    count = 0
    for ingredient in dish1:
        if ingredient in dish2:
            count += 1
        if count == 2:
            print('similar')
            break
    else:
        print('dissimilar')