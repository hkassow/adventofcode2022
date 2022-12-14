with open('inputs/input_day10.txt') as f:
    lines = f.readlines()

    res = 0

    signal = 1

    cycle = 0


    for line in lines:
        line = line.split('\n')[0]
        cycle += 1
        if (cycle-20)%40 == 0:
            res += (cycle*signal)
        if line != 'noop':
            cycle += 1
            if (cycle-20)%40 == 0:
                res += (cycle*signal)
            num = int(line.split(' ')[1])

            signal += num

    print('part1', res)

    crt = []
    curr_row = ''
    signal = 1
    cycle = 0
    for line in lines:
        line = line.split('\n')[0]
        if abs(cycle-signal) <= 1:
            curr_row += '#'
        else:
            curr_row += '.'
        cycle += 1
        if cycle%40 == 0:
            crt.append(curr_row)
            curr_row = ''
            cycle = 0

        if line != 'noop':
            if abs(cycle-signal) <= 1:
                curr_row += '#'
            else:
                curr_row += '.'
            cycle += 1
            if cycle%40 == 0:
                crt.append(curr_row)
                curr_row = ''
                cycle = 0
            num = int(line.split(' ')[1])
        
            signal += num
    print('part2')
    for row in crt:
        print(row)