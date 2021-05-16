for _ in range(int(input())):
    apples, oranges, coins = map(int, input().split())
    if apples > oranges:
        apples, oranges = oranges, apples
    while True:
        if apples == oranges or coins == 0:
            break
        apples += 1
        coins -= 1
    print(oranges - apples)