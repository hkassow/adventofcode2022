import collections
# part 1 
# find letter that appears twice 
# sum all letters 

with open('input_day3.txt') as f:
    lines = f.readlines()
    x = 0
    for line in lines:
        letter = set()
        let = -1
        firstHalf = line[0:len(line)//2]
        secondHalf = line[len(line)//2:]
        for c in firstHalf:
            letter.add(c)
        for c in secondHalf:
            if c in letter:
                let = c
                break
        if ord('a') <= ord(let):
            x += ord(let) - ord('a') + 1
        else:
            x += ord(let) - ord('A')+ 27
    print('part1', x)

    n = len(lines)
    groups = n//3
    badge_sum = 0

    for i in range(groups):
        x = lines[i*3]
        y = lines[i*3+1]
        z = lines[i*3+2]
        x1 = collections.Counter(x)
        x2 = collections.Counter(y)

        for c in z:
            if c in x1 and c in x2:
                if ord('a') <= ord(c):
                    badge_sum += ord(c) - ord('a') + 1
                else:
                    badge_sum += ord(c) - ord('A') + 27
                break
    print('part2', badge_sum)