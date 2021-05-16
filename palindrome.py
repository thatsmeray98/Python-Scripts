for i in range(int(input())):
    num = input()
    print('wins') if num == num[::-1] else print('loses')
