for _ in range(int(input())):
    n = int(input())
    length = list(map(int,input().split()))
    rating = list(map(int,input().split()))
    maxlr,maxr,ans = 0,0,0
    for i in range(n):
        if length[i]*rating[i] > maxlr:
            maxlr = length[i]*rating[i]
            maxr = rating[i]
            ans = i
        elif length[i]*rating[i] == maxlr:
            if rating[i]>maxr:
                maxr = rating[i]
                ans = i
    print(ans+1)