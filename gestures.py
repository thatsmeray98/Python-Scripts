for i in range(int(input())):
    count, gestures = int(input()), input()
    if 'I' in gestures:
        print('INDIAN')
    elif 'Y' in gestures:
        print('NOT INDIAN')
    else:
        print('NOT SURE')