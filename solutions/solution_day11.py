def buildFunction(list):

    def f(old):
        x,y = -1, -1
        if list[0] == 'old':
            x = old
        else:
            x = int(list[0])
        if list[2] == 'old':
            y = old
        else:
            y = int(list[2])
        
        if list[1] == '+':
            return x + y
        else:
            return x * y
    return f


with open('inputs/input_day11.txt') as f:
    lines = f.readlines()

    i = 0
    monkeys = []
    div_by = 1
    while i + 5 <= len(lines):
        items = lines[i+1].split(':')[1].split(',')
        items[-1] = items[-1].split('\n')[0]
        for j in range(len(items)):
            items[j] = int(items[j])

        params = lines[i+2].split('= ')[1].split(' ')
        params[-1] = params[-1].split('\n')[0]
        
        operation = buildFunction(params)


        divisble_by = int(lines[i+3].split(' ')[-1])
        div_by *= divisble_by
        true_monkey = int(lines[i+4].split(' ')[-1])
        false_monkey = int(lines[i+5].split(' ')[-1])
        
        monkeys.append([items, operation, divisble_by, true_monkey, false_monkey, 0])
        i += 7
    
    
    for i in range(10000):

        for i in range(len(monkeys)):
            monkey = monkeys[i]

            for item in monkey[0]:
                monkey[-1] += 1
                val = monkey[1](item)
                val %= div_by # for part1 replace this with dividing by 3 and rounding to nearest integer, and replace rounds with 20 instead of 10000
                if val%monkey[2] == 0:
                    monkeys[monkey[3]][0].append(val)
                else:
                    monkeys[monkey[4]][0].append(val)
            monkey[0] = []
        

    monkeys = sorted(monkeys, key=lambda x:x[5], reverse = True)
    print('part2', monkeys[0][-1] * monkeys[1][-1])