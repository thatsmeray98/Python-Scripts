for cases in range(int(input())):
    triangle = []
    for row in range(int(input())):
        triangle.append(list(map(int, input().split())))
    
    sum = [[0 for i in range(j+1)] for j in range(len(triangle))]
    for rowindex in range(len(triangle)):
        for numindex in range(rowindex+1):
            if rowindex==0 and numindex==0:
                sum[rowindex][numindex] = triangle[rowindex][numindex]
            elif numindex==0 :
                sum[rowindex][numindex] = triangle[rowindex][numindex] + sum[rowindex-1][numindex]
            elif numindex == rowindex:
                sum[rowindex][numindex] = triangle[rowindex][numindex] + sum[rowindex-1][numindex-1]
            else:
                sum[rowindex][numindex] = triangle[rowindex][numindex] + max(sum[rowindex-1][numindex-1],sum[rowindex-1][numindex])
    
    max_num = 0
    for row in sum:
        if max_num < max(row):
            max_num = max(row)
    print(max_num)
        
