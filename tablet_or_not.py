for _ in range(int(input())):
    tablets, budget = map(int,input().split())
    parameters = []
    for i in range(tablets):
        parameters.append(tuple(map(int,input().split())))
    max_area_in_budget = 0
    for param in parameters:
        if param[2] <= budget and param[0]*param[1] > max_area_in_budget:
            max_area_in_budget = param[0]*param[1]
    print('no tablet') if max_area_in_budget == 0 else print(max_area_in_budget)