def factors(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

for _ in range(int(input())):
    num1, num2 = map(int,input().split())
    count = 1
    while True:
        if factors(num1+num2+count):
            break
        count += 1
    print(count) 
