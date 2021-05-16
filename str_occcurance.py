for _ in range(int(input())):
    word = input()
    for i in set(word):
        if word.count(i) == len(word)-word.count(i):
            print('YES')
            break
    else:
        print('NO')
