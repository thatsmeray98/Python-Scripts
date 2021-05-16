for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())),reverse = True)
    count, area, i = 0, 1, 0
    while count < 2 and i<len(arr)-1:
        if arr[i]==arr[i+1] :
                area *= arr[i]
                count += 1
                i+=1
        i+=1
    print(area) if count == 2 else print(-1)