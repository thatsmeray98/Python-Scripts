for _ in range(int(input())):
    n,m = map(int,input().split())
    completed_jobs = input().split()
    chef,assistant = [],[]
    counter = True
    for i in range(1,n+1):
        if counter: chef.append(i)
        else: assistant.append(i)
        counter = not counter
    print(*chef)
    print(*assistant)
