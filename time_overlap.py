for _ in range(int(input())):
    student_count = int(input())
    time_moment = list(map(int, input().split()))
    cook_time = list(map(int, input().split()))
    count = 0
    for i in range(student_count):
        if (i == 0) and (time_moment[i] >= cook_time[i]):
            count += 1
        elif (i != 0) and (time_moment[i]-time_moment[i-1] >= cook_time[i]):
            count += 1
    print(count)
    