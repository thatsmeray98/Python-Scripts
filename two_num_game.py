for _ in range(int(input())):
    a,b,n = map(int,input().split())
    print(max(a,b)//min(a//b)) if n%2==0 else print(max(a*2,b)//min(a*2,b))