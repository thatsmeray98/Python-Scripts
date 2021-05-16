for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if set(arr) == {1, 2, 3, 4, 5, 6, 7} and arr[0] == 1 and arr == arr[::-1]:
        for i in range((len(arr)-1)//2):
            if arr[i] != arr[i+1] and arr[i]+1 != arr[i+1]:
                print('no')
                break
        else:
            print('yes')
    else:
        print('no')
