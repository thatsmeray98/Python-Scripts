for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    sub_arr = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if count < m:
            if sub_arr[count] == arr[i]:
                count += 1
        else:
            break
    if count == m:
        print('Yes')
    else:
        print('No')