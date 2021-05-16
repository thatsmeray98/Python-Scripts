import sys 
sys.setrecursionlimit(10**4)

def maxsqr(base):
    count = 0
    if base-2 >= 2:
        maxsqr(base-2)
    count = (base-2)//2
    return count*(count+1)//2
        
for i in range(int(input())):
    print(maxsqr(int(input())))
