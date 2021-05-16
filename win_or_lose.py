# Valid for all kinda inputs (even invalid matches)
'''
for _ in range(int(input())):
    s = input()
    if len(s) < 20:
        print('WIN') if s.count('1') > s.count('0') else print('LOSE')
    else:
        for i in range(len(s[20:])):
            if s[i]=='0'and s[i+1]=='0':
                print('LOSE')
                break
            elif s[i]=='1'and s[i+1]=='1':
                print('WIN')
                break
'''
# Valid for only verified inputs with valid matches
for _ in range(int(input())):
    s = input()
    print('WIN') if s.count('1') > s.count('0') else print('LOSE')