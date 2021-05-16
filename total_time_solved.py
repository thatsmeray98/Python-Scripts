from math import ceil
for _ in range(int(input())):
    problems, break_time, time_per_problem = map(int, input().split())
    total_time, problems_solved = 0, 0
    while problems != 0:
        problems_solved = ceil(problems/2)
        problems -= problems_solved
        total_time += problems_solved * time_per_problem + break_time
        time_per_problem *= 2
    print(total_time-break_time)