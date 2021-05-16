for _ in range(int(input())):
    cats, dogs, leg_count = map(int,input().split())
    min_legs = dogs*4
    if cats > 2*dogs:
        min_legs += (cats - (2*dogs))*4
    print('yes') if leg_count%4 == 0 and leg_count >= min_legs and leg_count <= (cats+dogs)*4 else print('no')