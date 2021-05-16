for _ in range(int(input())):
    s = input()
    odd_elem = [i for i in range(len(s)) if i%2 != 0]
    even_elem = [i for i in range(len(s)) if i%2 == 0]
    print('YES') if len(odd_elem) == s.count(s[0]) and len(even_elem) == s.count(s[1]) and s[0]!=s[1] else print('NO')
    