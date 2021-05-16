for _ in range(int(input())):
    num, arr = int(input()), sorted(list(map(int,input().split())))
    print(arr[0]*(len(arr)-1))