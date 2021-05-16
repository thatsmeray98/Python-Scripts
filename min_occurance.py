for i in range(int(input())):
    balloons = input()
    print(balloons.count('a')) if balloons.count('a') < balloons.count('b') else print(balloons.count('b'))