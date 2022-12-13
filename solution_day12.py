def solveDay12(grid):
    m = len(grid)
    n = len(grid[0])
    queue = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'a' or grid[i][j] == 'S':
                queue.append([i,j])
                grid[i][j] = 97
    neighbor = [[1,0], [0,1], [-1,0], [0,-1]]
    
    steps = 0
    while queue:
        next_level = []
        steps += 1

        for i,j in queue:
            for rc,cc in neighbor:
                r,c = i+rc, j+cc
                if r < 0 or c < 0 or r == m or c == n or type(grid[r][c]) == int:
                    continue
                if grid[r][c] == 'E': 
                    if grid[i][j] >= 121:
                        return steps
                    else:
                        continue
                elif (ord(grid[r][c]) - grid[i][j]) > 1:
                    continue

                grid[r][c] = ord(grid[r][c])
                next_level.append([r,c])
        queue = next_level

#part 1 involes solving just from 'S'
#part 2 involves solving from any 'a' or 'S'
with open('input_day12.txt') as f:
    lines = f.readlines()

    grid = []

    for line in lines:
        row = list(line)
        if row[-1] == '\n':
            row.pop()
        
        grid.append(row)
    print(solveDay12(grid))