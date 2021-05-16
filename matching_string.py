for _ in range(int(input())):
    x,y,count = input(),input(),0
    for i in range(len(x)):
        if x[i]==y[i] or (x[i] != y[i] and (x[i]=='?' or y[i]=='?')):
            count += 1
            continue
        else:
            print('No')
            break
    if count == len(x):
        print('Yes')