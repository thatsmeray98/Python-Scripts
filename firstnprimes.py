n = int(input())
nprimes = [1]
for i in range(n):
    for j in range(2,i//2): 
        if i%j==0: 
            nprimes.append(i)
print(nprimes)
