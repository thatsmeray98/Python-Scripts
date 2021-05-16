for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    alt_seq = [1]*n
    for i in range(len(lst)-2,-1,-1):
        if lst[i]*lst[i+1]<0:
            alt_seq[i] += alt_seq[i+1]
    print(*alt_seq)
