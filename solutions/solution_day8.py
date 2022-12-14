with open('inputs/input_day8.txt') as f:
    lines = f.readlines()

    grid = []

    for line in lines:
        line = list(line)
        if line[-1] == '\n':
            line.pop()
        grid.append(line)
    res = len(grid)*2 + len(grid[0])*2 -4
    
    
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            
            curr_tree = grid[i][j]
            if max(grid[i][0:j]) < curr_tree or max(grid[i][j+1:]) < curr_tree or max(row[j] for row in grid[:i]) < curr_tree or max(row[j] for row in grid[i+1:]) < curr_tree:
                res += 1
    print('part1', res)
    
    mx = -1
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):

            curr_tree = grid[i][j]
            left,right,up,below = 0,0,0,0
            
            for x in range(j-1,-1,-1):
                left += 1
                if grid[i][x] >= curr_tree:
                    break
            for x in range(j+1, len(grid[0])):
                right += 1
                if grid[i][x] >= curr_tree:
                    break
            for y in range(i-1,-1,-1):
                up += 1
                if grid[y][j] >= curr_tree:
                    break
            for y in range(i+1, len(grid[0])):
                below += 1
                if grid[y][j] >= curr_tree:
                    break
            mx = max(mx, left*right*up*below)
    print('part2', mx)