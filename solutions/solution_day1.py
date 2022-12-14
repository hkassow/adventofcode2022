from heapq import heappush, heappop

# advent problem day 1
# find the elf carrying the most calories
# part 2 find the top 3 

with open('inputs/input_day1.txt') as f:
    lines = f.readlines()
    calories = []
    curr = 0
    for i in lines:
        if i == '\n':
            heappush(calories, -curr)
            curr = 0
        else:
            curr += int(i)
    x = -heappop(calories)
    print('part1', x)
    print('part2', x + -heappop(calories) + -heappop(calories))