for i in range(int(input())):
    hardness, carbon, tensile = map(float,input().split())
    a, b, c = hardness > 50, carbon < 0.7, tensile > 5600
    if a and b and c:
        print(10)
    elif a and b:
        print(9)
    elif b and c:
        print(8)
    elif a and c:
        print(7)
    elif a or b or c:
        print(6)
    else:
        print(5)
    