for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    operations = 0
    for i in arr:
        if i%k != 0:
            if i%k <= k//2:
                operations += i%k
            elif i%k > k//2:
                operations += k-(i%k)
    print(operations)