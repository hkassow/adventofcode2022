with open('input_day4.txt') as f:
    lines = f.readlines()
    res = 0
    res1 = 0
    checked = [-1 for i in range(100)]    
    
    for line in lines:
        ranges = []
        i = 0
        while i < len(line):
            if line[i].isnumeric():
                j = i
                curr_num = 0
                while j < len(line) and line[j].isnumeric():
                    curr_num *= 10
                    curr_num += int(line[j])
                    j += 1
                i = j-1
                ranges.append(curr_num)
            i+=1
        if (ranges[0] <= ranges[2] and ranges[3] <= ranges[1]) or (ranges[2] <= ranges[0] and ranges[1] <= ranges[3]):
            res += 1
        if min(ranges[1], ranges[3]) - max(ranges[0], ranges[2]) >= 0:
            res1 += 1
    print(res, res1)
        