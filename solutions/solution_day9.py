def move(command, count, head, tails, visited):
    for i in range(count):
        if command == 'L':
            head[1] -= 1
        elif command == 'R':
            head[1] += 1 
        elif command == 'U':
            head[0] -= 1  
        else:
            head[0] += 1
        moveTails(head, tails,visited)
def moveTails(head, tails, visited):
    prev = head
    curr = 0
    while curr < len(tails):
        if abs(prev[0] - tails[curr][0]) >= 2 and abs(prev[1] - tails[curr][1]) >= 2:
            if tails[curr][0] < prev[0]:
                tails[curr][0] = prev[0] -1
            else:
                tails[curr][0] = prev[0] + 1

            if tails[curr][1] < prev[1]:
                tails[curr][1] = prev[1] - 1
            else:
                tails[curr][1] = prev[1] + 1

        elif abs(prev[0] - tails[curr][0]) >= 2:
            tails[curr][1] = prev[1]
            if tails[curr][0] < prev[0]:
                tails[curr][0] = prev[0] -1
            else:
                tails[curr][0] = prev[0] + 1
        elif abs(prev[1] - tails[curr][1]) >= 2:
            tails[curr][0] = prev[0]
            if tails[curr][1] < prev[1]:
                tails[curr][1] = prev[1] - 1
            else:
                tails[curr][1] = prev[1] + 1
        prev = tails[curr]
        curr += 1
    visited.add(tuple(tails[-1]))






with open('inputs/input_day9.txt') as f:
    lines = f.readlines()

    head = [0,0]
    tails = [[0,0]]
    visited = set()
    visited.add(tuple([0,0]))

    head2 = [0,0]
    tails2 = [[0,0] for i in range(9)]
    visited2 = set()
    visited2.add(tuple([0,0]))
    
    for line in lines:
        command,count = line.split(' ')
        move(command, int(count), head, tails, visited)
        move(command, int(count), head2, tails2, visited2)
    
    print('part1', len(visited))
    print('part2', len(visited2))