"""
def gcd(x,y):
    if x<y:
        x,y = y,x
    if x%y==0:
        return y
    else:
        return gcd(x,x%y)

def lcm(x,y):
    return int((x*y)/gcd(x,y))
"""
from math import gcd
for i in range(int(input())):
    x,y = map(int,input().split())
    print(gcd(x,y),int((x*y)/gcd(x,y)))
