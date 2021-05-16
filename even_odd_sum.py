for _ in range(int(input())):
    odd, even = map(int, input().split())
    odd_sum, even_sum = 1, 2
    while True:
        odd -= odd_sum
        even -= even_sum
        if odd < 0:
            print("Bob")
            break
        elif even < 0:
            print("Limak")
            break
        odd_sum += 2
        even_sum += 2
