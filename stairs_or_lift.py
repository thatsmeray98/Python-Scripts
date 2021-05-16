for _ in range(int(input())):
    flours, vstair, vlift = map(int, input().split())
    print('Elevator') if (flours*(2**0.5))/vstair > 2*(flours/vlift) else print('Stairs')