x,y = int(input()), int(input())
if x*y > 2*(x+y):
    print('Area')
    print(x*y)
elif 2*(x+y) > x*y:
    print('Peri')
    print(2*(x+y))
else:
    print('Eq')        
    print(x*y)