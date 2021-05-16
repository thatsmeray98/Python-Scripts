for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(len(arr)):
        sum, product = 0, 1
        for j in range(i,len(arr)):
            sum += arr[j]
            product *= arr[j]
            if sum == product:
                count += 1
    print(count)
