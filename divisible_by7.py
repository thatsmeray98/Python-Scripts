for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    for i in arr:
        if (i+k)%7==0:
            count += 1
    print(count)    