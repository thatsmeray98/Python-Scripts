vowel = ('a','e','i','o','u')
for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    count, i = 0, 0
    while i < n:
        if s[i] not in vowel and s[i+1] in vowel:
            count += 1
            i += 1
        i += 1
    print(count)