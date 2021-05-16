arr = list(map(int,input().split()))
count = 0
for x in arr:
    if int(round(abs(x) ** (1 / 3))) ** 3 == abs(x):
        count += 1
print(count)

