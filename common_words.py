for _ in range( int(input())):
    n,k = map(int,input().split())
    words = list(map(str,input().split()))
    phrase = []
    for _ in range(k):
        phrase.extend(list(map(str,input().split())))
    for word in words:
        if word in phrase:
            print('YES', end = ' ')
        else:
            print('NO', end = ' ')
    print()