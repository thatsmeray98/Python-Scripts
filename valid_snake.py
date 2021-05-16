for _ in range(int(input())):
    n = int(input())
    report = input().replace('.','')
    print(report)
    if len(report)%2 == 0:
        for i in range(len(report)):
            if (i%2==0 and report[i] != 'H') or (i%2!=0 and report[i] != 'T'):
                print('Invalid')
                break
    else:
        print('Valid')