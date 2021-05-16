for _ in range(int(input())):
    ans = 0
    for num in range(1,int(input())+1):
        input()
        ans ^= num
    print(ans)