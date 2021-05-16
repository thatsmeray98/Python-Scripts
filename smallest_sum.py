for i in range(int(input())):
    count, arr = int(input()), list(map(int, input().split())) 
    print(sorted(arr)[0]+sorted(arr)[1])
