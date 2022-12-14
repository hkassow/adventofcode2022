import bisect

with open('inputs/input_day7.txt') as f:
    lines = f.readlines()

    root_dir = {'files':[]}
    curr_dir = root_dir

    for command in lines:
        command = command.split(' ')
        command[-1] = command[-1].split('\n')[0]
        if command[0] == '$':
            if command[1] == 'ls':
                continue
            elif command[2] == '/':
                curr_dir = root_dir
            elif command[2] == '..':
                curr_dir = curr_dir['parent']
            else:
                curr_dir = curr_dir[command[2]]
        else:
            if command[0] == 'dir':
                curr_dir[command[1]] = {'parent': curr_dir, 'files':[]}
            else:
                curr_dir['files'].append(tuple([int(command[0]), command[1]]))

    def getTotal():
        res1 = 0
        dir_sizes = []
        def findSmallDir(dir):
            nonlocal res1, dir_sizes
            size = 0
            for key in dir:
                if key == 'parent' or key == 'files':
                    continue
                size += findSmallDir(dir[key])
            
            for x in dir['files']:
                size += x[0]
            if size <= 100000:
                nonlocal res1
                res1 += size
            dir_sizes.append(size)
            return size

        
        used_space = findSmallDir(root_dir)
        print('part1', res1)
        space_needed = 30000000 - (70000000-used_space)

        dir_sizes.sort()
        print('part2', dir_sizes[bisect.bisect_left(dir_sizes, space_needed)])
    getTotal()
        
    