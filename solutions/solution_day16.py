with open('inputs/input_day16.txt') as f:
    lines = f.readlines()

    graph = {}
    flow_rate = {}

    for line in lines:
        line = line.split(' ')
        valve = line[1]
        rate = line[4].split('=')[1].split(';')[0]
        paths = []
        j = -1
        while line[j] != 'valve' and line[j] != 'valves':
            paths.append(line[j].split('\n')[0].split(',')[0])
            j -= 1
        graph[valve] = paths
        flow_rate[valve] = int(rate)

    
    opened = set()
    arrived = {key:[-1 for i in range(30)] for key in graph}

    def openValves(valve, opened, minute, flow, curr_rate, parent):
        if minute >= 30:
            return flow
        if curr_rate < arrived[valve][minute] and valve in opened:
            return flow
        

        arrived[valve][minute] = curr_rate

        mx = flow
        
        for path in graph[valve]:
            if path == parent:
                continue
            mx = max(openValves(path, opened, minute+1, flow+curr_rate, curr_rate, valve), mx)
        if valve not in opened and flow_rate[valve] != 0 and minute < 29:
            opened.add(valve)
            minute += 1
            flow += curr_rate
            curr_rate += flow_rate[valve]
            
            for path in graph[valve]:
                mx = max(openValves(path, opened, minute+1, flow+curr_rate, curr_rate, valve), mx)
            
            opened.remove(valve)
            
        return mx
    print(openValves('AA', opened, 0, 0, 0 , -1))
        