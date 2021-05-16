for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    addition = []
    for i in range(n):
        for j in range(i+1,n):
            addition.append(sum(list(map(int,str(arr[i]*arr[j])))))
    print(max(addition))