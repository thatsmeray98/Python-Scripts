for _ in range(int(input())):
    circle_count = int(input())
    square_count = 0
    while circle_count > 0:
        circle_count -= int(circle_count**0.5) **2
        square_count += 1
    print(square_count)