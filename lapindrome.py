for i in range(int(input())):
    word = input()
    if len(word)%2 == 0:
        for alphabet in word[:len(word)//2]:
            if word[:len(word)//2].count(alphabet) != word[len(word)//2:].count(alphabet):
                print('NO')
                break
        else:
            print('YES')
    else:
        for alphabet in word[:len(word)//2]:
            if word[:len(word)//2].count(alphabet) != word[len(word)//2+1:].count(alphabet):
                print('NO')
                break
        else:
            print('YES')
