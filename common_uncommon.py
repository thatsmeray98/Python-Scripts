for _ in range(int(input())):
    n,m,k = map(int,input().split())
    universal = set([i for i in range(1,n+1)])
    ignored = set(map(int,input().split()))
    tracked = set(map(int,input().split()))
    print(len(ignored.intersection(tracked)), len(universal-(ignored.union(tracked))))
