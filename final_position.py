for _ in range(int(input())):
    n = int(input())
    x_axis, y_axis = 0, 0
    x, y = 0, 0
    for i in input():
        if i == 'L' and x_axis == 0:
            x -= 1
            x_axis, y_axis = 1, 0
        elif i == 'R' and x_axis == 0:
            x += 1
            x_axis, y_axis = 1, 0
        elif i == 'U' and y_axis == 0:
            y += 1
            x_axis, y_axis = 0, 1
        elif i == 'D' and y_axis == 0:
            y -= 1
            x_axis, y_axis = 0, 1
    print(x, y)
'''
# Another method with 1 less variable.

for _ in range(int(input())):
    n = int(input())
    counter = 0
    x,y = 0,0
    for i in input():
        if i=='L'and counter != 1:
            x-=1
            counter = 1
        elif i=='R' and counter != 1:
            x+=1
            counter = 1
        elif i=='U' and counter != -1:
            y+=1
            counter = -1
        elif i=='D' and counter != -1:
            y-=1
            counter = -1
    print(x,y)
'''