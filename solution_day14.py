import math

with open('input_day14.txt') as f:
    lines = f.readlines()
    rock_cord = []
    x_min = math.inf
    x_max = -1
    y_max = -1
    for line in lines:
        line = line.split('->')
        line[-1] = line[-1].split('\n')[0]
        for i in range(len(line)):
            x = line[i]
            x = line[i].split(',')
            x = [int(x[0]), int(x[1])]
            x_min = min(x[0], x_min)
            x_max = max(x[0], x_max)
            y_max = max(y_max, x[1])
            line[i] = x
        rock_cord.append(line)
    

    cave = [['.' for j in range(x_max-x_min+1)] for i in range(y_max+1)]

    for formation in rock_cord:
        
        prev = formation[0]

        for i in range(1, len(formation)):
            curr = formation[i]

            if curr[0] == prev[0]:
                c = curr[0] - x_min
                for j in range(min(prev[1], curr[1]),max(prev[1],curr[1])+1):
                    r = j
                    cave[r][c] = '#'
            else:
                r = curr[1]
                for i in range(min(prev[0], curr[0]), max(prev[0], curr[0])+1):
                    c = i - x_min
                    cave[r][c] = '#'
            prev = curr
    
    
    def dropDown(r,c, grid):

        adj = [[1,0], [1,-1], [1,1]]

        while True:
            did_drop = False
            for rc,cc in adj:
                i,j = r+rc,c+cc
                if i == len(grid) or j < 0 or j == len(grid[0]):
                    #this condition should only be triggered during part 1 calculation
                    return False
                if grid[i][j] ==  '.':
                    did_drop = True
                    r = i 
                    c = j
                    break
            if not did_drop:
                grid[r][c] = '+'
                #this condition should only be triggered during part 2 condition
                if r == 0 and c == 500:
                    print('done')
                    return False
                return True
    res = 0
    while dropDown(0,500-x_min,cave):
        res += 1
    print('part1', res)

    

    # part 2 obeservation the farthest the sand can go is +- y_max+2 otherwise it will have reached the top and can't fall anymore
    # rounded to 750 per row  
    # part2 we keep the original coordinates intact and dont down shift all the columns

    cave2 = [['.' for j in range(750)] for i in range(y_max+3)]

    for formation in rock_cord:
        
        prev = formation[0]

        for i in range(1, len(formation)):
            curr = formation[i]

            if curr[0] == prev[0]:
                c = curr[0]
                for j in range(min(prev[1], curr[1]),max(prev[1],curr[1])+1):
                    r = j
                    cave2[r][c] = '#'
            else:
                r = curr[1]
                for i in range(min(prev[0], curr[0]), max(prev[0], curr[0])+1):
                    c = i
                    cave2[r][c] = '#'
            prev = curr
    cave2[-1] = ['#' for j in range(1000)]
    res2 = 0
    while dropDown(0,500,cave2):
        res2 += 1
    print('part2', res2+1)