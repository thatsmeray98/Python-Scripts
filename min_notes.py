notes = [100,50,10,5,2,1]
for i in range(int(input())):
    amount = int(input())
    total, count = 0, 0
    restart = True
    while restart:
        for note in notes:
            if total+note <= amount:
                total += note
                count += 1
                restart = True
                break
            restart = False
    print(count)
