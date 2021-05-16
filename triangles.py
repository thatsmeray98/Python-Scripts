for _ in range(int(input())):
    coins, rows = int(input()), 0
    while coins > rows:
        rows += 1
        coins -= rows
    print(rows)    
