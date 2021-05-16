num = input()
if int(num) >= 10:
    new_num = num[-2:]
    print(int(num)+1) if int(new_num) % 4 == 0 else print(int(num)-1)
else:
    print(int(num)+1) if int(num)%4 == 0 else print(int(num)-1)
    