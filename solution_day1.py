from heapq import heappush, heappop

# advent problem day 1
# find the elf carrying the most calories
# part 2 find the top 3 

with open('input_day1') as f:
    lines = f.readlines()
    calories = []
    curr = 0
    for i in lines:
        if i == '\n':
            heappush(calories, -curr)
            curr = 0
        else:
            curr += int(i)
    print(-heappop(calories), -heappop(calories), -heappop(calories))
