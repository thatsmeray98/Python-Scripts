for i in range(int(input())):
    max_range, distances, count = float(input()), [], 0
    (x1, y1), (x2, y2), (x3, y3) = map(int, input().split()), map(int, input().split()), map(int, input().split())
    first_dist, second_dist, third_dist = ((x1-x2)**2 + (y1-y2)**2)**0.5, ((x2-x3)**2 + (y2-y3)**2)**0.5, ((x3-x1)**2 + (y3-y1)**2)**0.5
    print('yes') if (first_dist <= max_range and second_dist <= max_range) or (third_dist <= max_range and first_dist <= max_range) or (second_dist <= max_range and third_dist <= max_range) else print('no')        
