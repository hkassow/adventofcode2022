with open('inputs/input_day15.txt') as f:
    lines = f.readlines()


    def findMaxDist(i,j,bi,bj):
        dist = abs(i-bi) + abs(j-bj)


        return dist
    def combineSpreads(spreads):

        spreads = sorted(spreads, key=lambda x:x[0])

        combined = [spreads[0]]

        for spread in spreads:
            if spread[0] <= combined[-1][1]:
                combined[-1][1] = max(spread[1], combined[-1][1])
            else:
                combined.append(spread)
        return combined
    position_no_beacon = set()
    position_beacon = set()

    for line in lines:
        sensor, beacon = line.split(':')
        sensor = sensor.split(' ')
        beacon = beacon.split(' ')
        sensor_x, sensor_y = int(sensor[-2].split('=')[1].split(',')[0]), int(sensor[-1].split('=')[1])
        beacon_x, beacon_y = int(beacon[-2].split('=')[1].split(',')[0]), int(beacon[-1].split('=')[1].split('\n')[0])
        beacon_pos =tuple([beacon_x, beacon_y])
        position_beacon.add(beacon_pos)

        if beacon_pos in position_no_beacon:
            position_no_beacon.remove(beacon_pos)

        max_dist = findMaxDist(sensor_x, sensor_y,beacon_x,beacon_y)

        y_dist = abs(sensor_y-2000000)

        x_dist = max_dist - y_dist

        if x_dist < 0:
            continue
        
        for i in range(x_dist+1):
            tup = tuple([sensor_x+i, 2000000])
            tup1 = tuple([sensor_x-i, 2000000])
            if tup not in position_beacon:
                position_no_beacon.add(tup)
            if tup1 not in position_beacon:
                position_no_beacon.add(tup1)
        
    print('part1', len(position_no_beacon))
    
    sensors = []
    for line in lines:
        sensor, beacon = line.split(':')
        sensor = sensor.split(' ')
        beacon = beacon.split(' ')
        sensor_x, sensor_y = int(sensor[-2].split('=')[1].split(',')[0]), int(sensor[-1].split('=')[1])
        beacon_x, beacon_y = int(beacon[-2].split('=')[1].split(',')[0]), int(beacon[-1].split('=')[1].split('\n')[0])
        
        

        max_dist = findMaxDist(sensor_x, sensor_y, beacon_x, beacon_y)

        sensors.append([sensor_x, sensor_y, max_dist])
    

    for y in range(4000001):

        covered = []

        for sensor in sensors:
            max_x_dist = sensor[2] - abs(y - sensor[1])
            if max_x_dist < 0:
                continue
            spread = [max(0, sensor[0]-max_x_dist), min(4000000, sensor[0] + max_x_dist)]
            covered.append(spread)
        covered = combineSpreads(covered)
        
        if len(covered) == 1:
            continue
        else:
            if 0 < covered[0][0]:
                print(0,y)
            elif covered[-1][1] < 4000000:
                print(4000000,y)
            else:
                print('part2', (covered[0][1]+1)*4000000+y)
            break
