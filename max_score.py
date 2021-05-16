for _ in range(int(input())):
    n = int(input())
    goals = list(map(int,input().split()))
    fouls = list(map(int,input().split()))
    scorecard = list(zip(goals,fouls))
    score = []
    for goal, foul in scorecard:
        score.append(goal*20 - foul*10)
    print(0) if max(score)<0 else print(max(score))