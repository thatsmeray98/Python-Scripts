x = int(input())
for i in range(x):
    num = input()
    if int(num)%10 != 0:
        print(num[::-1])
    else:
        count = 0
        for i in num[::-1]:
            if i=='0':
                count+=1
            else: 
                break
        print(num[:-count][::-1])
