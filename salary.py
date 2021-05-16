for i in range(int(input())):
    num = int(input())
    print(num+(0.1*num)+(0.9*num)) if num < 1500 else print(num+500+(0.98*num))
