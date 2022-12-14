with open('inputs/input_day5.txt') as f:
    lines = f.readlines()
    x = [[] for i in range(10)]
    for i in range(7,-1,-1):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c == ' ' or c == '[' or c == ']' or c == '\n':
                continue
            x[(j-1)//4 + 1].append(c)

    for moves in lines[10:]:
        nums = []

        i = 0
        while i < len(moves):
            if moves[i].isnumeric():
                curr_num = 0

                while i < len(moves) and moves[i].isnumeric():
                    curr_num *= 10
                    curr_num += int(moves[i])
                    i += 1
                i -= 1
                nums.append(curr_num)
            i += 1
        count = nums[0]
        start = nums[1]
        destination = nums[2]

        # for part2 since we can move multiple crates at the same time create list and append every crate into its correct position
        # the first crate popped will go to 0-1 => last index which means it will be on top of its new stack
        # we use the compliment to get its correct position in the array 
        
        addingToStack = [0 for x in range(count)]

        for k in range(min(count, len(x[start]))):
            #x[destination].append(x[start].pop()) part1 moving only 1 crate at a time we can simply pop + append the top crate

            addingToStack[~k] = x[start].pop()

        x[destination] += addingToStack
    
    word = ''
    for stack in x:
        if len(stack) == 0:
            continue
        word += stack[-1]
    print(word)
    