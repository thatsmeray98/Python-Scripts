count = int(input())
even_count, odd_count = 0,0
for num in list(map(int,input().split())):
    if num%2 == 0:
        even_count += 1
    else: 
        odd_count += 1
print('READY FOR BATTLE') if even_count > odd_count else print('NOT READY') 
