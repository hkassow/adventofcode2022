with open('inputs/input_day6.txt') as f:

    line = f.readline()
    print(line)
    part1 = -1
    for i in range(len(line)):
        a,b,c,d = line[i], line[i+1], line[i+2], line[i+3]
        x = set([a,b,c,d])
        if len(x) == 4:
            if part1 == -1:
                part1 = i+4
        else:
            continue
        for k in range(14):
            x.add(line[i+k])
        if len(x) == 14:
            print('part1', part1)
            print('part2', i+14)
            break

