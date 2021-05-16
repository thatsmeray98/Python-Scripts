x = int(input())
arr = []
for i in range(x):
    arr.append(list(map(int, input().split())))
for i in range(len(arr)):
    if i!=0:
        arr[i][0] += arr[i-1][0]
        arr[i][1] += arr[i-1][1]
    if arr[i][0]-arr[i][1] > 0:
        arr[i].extend([1, arr[i][0]-arr[i][1]])
    else:
        arr[i].extend([2,arr[i][1]-arr[i][0]])
arr = sorted(arr, key = lambda x:x[3], reverse = True)
print(arr[0][2],arr[0][3])