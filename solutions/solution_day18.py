import json
with open('inputs/input_day18.txt') as f:
    lines = f.readlines()

    cubes1 = set()

    for line in lines:
        a,b,c = line.split(',')
        cubes1.add(tuple([int(a),int(b),int(c)]))
    
    res = 0

    for cube in cubes1:
        sides = 6
        a,b,c = cube
        side_tuples = []
        side_tuples.append(tuple([a+1,b,c]))
        side_tuples.append(tuple([a-1,b,c]))
        side_tuples.append(tuple([a,b+1,c]))
        side_tuples.append(tuple([a,b-1,c]))
        side_tuples.append(tuple([a,b,c+1]))
        side_tuples.append(tuple([a,b,c-1]))
        
        for side in side_tuples:
            if side in cubes1:
                sides -= 1
        res += sides
    print('part1', res)
    def isClosed(i,j,k):
        queue = [[i,j,k]]
        island = [[i,j,k]]
        visited = set()
        visited.add(tuple([i,j,k]))
        while queue:
            neighbors = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
            x,y,z = queue.pop()
            for xc,yc,zc in neighbors:
                xn,yn,zn = x+xc,y+yc,z+zc
                if xn < 0 or yn < 0 or zn < 0 or xn == 22 or yn == 22 or zn == 22:
                    return False
                if pool[xn][yn][zn] == 1 or tuple([xn,yn,zn]) in visited:
                    continue
                island.append([xn,yn,zn])
                queue.append([xn,yn,zn])
                visited.add(tuple([xn,yn,zn]))
        for x,y,z in island:
            pool[x][y][z] = 1
        return True

    pool = [[[0 for i in range(23)] for j in range(23)] for j in range(23)]
    cubes = []
    for line in lines:
        a,b,c = line.split(',')
        cubes.append([int(a), int(b), int(c)])
        pool[int(a)][int(b)][int(c)] = 1
    
    for i in range(22):
        for j in range(22):
            for k in range(22):
                if pool[i][j][k] == 1:
                    continue
                x = isClosed(i,j,k)
    res2 = 0
    for x,y,z in cubes:

        side = 6
        if pool[x+1][y][z] == 1:
            side -= 1
        if pool[x-1][y][z] == 1:
            side -= 1
        if pool[x][y+1][z] == 1:
            side -= 1
        if pool[x][y-1][z] == 1:
            side -= 1
        if pool[x][y][z+1] == 1:
            side -= 1
        if pool[x][y][z-1] == 1:
            side -= 1
        res2 += side
    print('part2', res2) 