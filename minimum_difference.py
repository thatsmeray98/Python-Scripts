for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    small = arr[0]
    for i in range(n-1):
        for j in range(i+1,n):
            if small > abs(arr[i]-arr[j]):
                small = abs(arr[i]-arr[j])
    print(small)