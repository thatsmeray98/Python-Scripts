for _ in range(int(input())):
    str1, str2, max, min = input(), input(), 0, 0
    for i in range(len(str1)):
        if str1[i]=='?' or str2[i]=='?':
            max += 1
        elif str1[i]!=str2[i]:
            min +=1
            max +=1 
    print(min,max)    
