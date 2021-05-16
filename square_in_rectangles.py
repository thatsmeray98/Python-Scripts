from math import gcd
for _ in range(int(input())):
    length, breadth = map(int,input().split())
    square_side = gcd(length,breadth)
    print(int((length/square_side)*(breadth/square_side)))