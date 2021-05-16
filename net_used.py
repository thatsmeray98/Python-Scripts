for _ in range(int(input())):
    n, free_min = map(int,input().split())
    usage = 0
    for i in range(n):
        time, speed = map(int,input().split())
        if time>= free_min:
            time -= free_min
            free_min = 0
        else :
            free_min -= time
            time = 0
        usage += time*speed
    print(usage)