def compareList(x,y):
    for i in range(len(x)):
        if i == len(y):
            return False
        result = -1
        if type(x[i]) == list and type(y[i]) == list:
            result = compareList(x[i], y[i])
        elif type(x[i]) == list:
            result = compareList(x[i], [y[i]])
        elif type(y[i]) == list:
            result = compareList([x[i]], y[i])
        else:
            if x[i] == y[i]:
                result = 'next'
            elif x[i] < y[i]:
                result = True
            else:
                result = False
        if result == 'next':
            continue
        else: 
            return result
    return True if len(x) < len(y) else 'next'



        
# part 1
# using json.load to parse our string lists
# '[a,b,c]' => [a,b,c]
# custom comparison function to compare each pair 
import json

with open('input_day13.txt') as f:
    lines = f.readlines()
    res = 0
    n = 0
    pair = 1
    while n < len(lines):
        left = json.loads(lines[n])
        right = json.loads(lines[n+1])
        compare = compareList(left,right)
        if compare:
            res += pair
        n += 3
        pair += 1
    print('part1', res)


# part 2 
# using heap to sort all the packets
# create custom class and use our previous comparison function to get them in order

from heapq import heappush, heappop

class Node(list):
    def __init__(self, packet: list):
        self.packet = packet
    def __lt__(self, other):
        return compareList(self.packet, other.packet)

with open('input_day13.txt') as f:
    lines = f.readlines()
    hp = []
    for x in lines:
        if x == '\n':
            continue
        line = json.loads(x)
        heappush(hp, Node(line))
    heappush(hp, Node([[2]]))
    heappush(hp, Node([[6]]))
    a = -1
    b = -1
    count = 1
    while hp:
        x = heappop(hp).packet
        if x == [[2]]:
            a = count
        if x == [[6]]:
            b = count
            break
        count += 1
    print('part2', a*b)