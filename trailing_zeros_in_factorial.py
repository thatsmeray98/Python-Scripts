for _ in range(int(input())):
    n = int(input())
    i, zeros = 1, 0
    while n//(5**i)!= 0:
        zeros += n//(5**i)
        i += 1
    print(zeros)