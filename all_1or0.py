for _ in range(int(input())):
    num = input()
    print('Yes') if num.count('0') == 1 or num.count('1') == 1 else print('No')