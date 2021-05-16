for i in range(int(input())):
    pattern = list(map(int, input().split()))
    minimum = min(pattern[1:])
    while minimum:
        if all([num % minimum == 0 for num in pattern[1:]]):
            print(*[num//minimum for num in pattern[1:]])
            break
        minimum -= 1