for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = [1]*n
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            new_arr[i] = new_arr[i-1]+1
    print(sum(new_arr))