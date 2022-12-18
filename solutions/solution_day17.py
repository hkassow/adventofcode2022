with open('inputs/input_day17.txt') as f:
    jets = f.readlines()[0]
    rocks = {}
    rocks[-1] = set()
    for i in range(7):
        rocks[-1].add(i)
    
    rock_form = [
        [[0,2],[0,3],[0,4],[0,5]],
        [[1,2],[0,3],[1,3],[2,3],[1,4]],
        [[0,2],[0,3],[0,4],[1,4],[2,4]],
        [[0,2],[1,2],[2,2],[3,2]],
        [[0,2],[1,2],[0,3],[1,3]]]

    def dropRock(rock,j):
        x_shift = 0
        y_shift = 0
        while True:
            if j == len(jets):
                j = 0
            jet_dir = 1 if jets[j] == '>' else -1
            broke = False
            for y,x in rock:
                if  x+x_shift+jet_dir == 7 or x+x_shift+jet_dir < 0 or (y+y_shift in rocks and x+x_shift+jet_dir in rocks[y+y_shift]):
                    broke = True
                    break
            j += 1
            if not broke:
                x_shift += jet_dir
            
            broke = False
            for y,x in rock:
                if y+y_shift-1 in rocks and x+x_shift in rocks[y+y_shift-1]:
                    broke = True
                    break
            if not broke:
                y_shift -= 1
            else:
                return [rock, j,x_shift, y_shift]
    
    min_height = 0
    j = 1133
    curr_form = 1
    store = []
    for i in range(1675):
        form = rock_form[curr_form]
        curr_rock = []
        curr_form += 1
        curr_form %= 5
        
        for y,x in form:
            curr_rock.append([y+min_height+3, x])
        curr_rock,j,x_shift,y_shift = dropRock(curr_rock,j)
        reset = -1
        for y,x in curr_rock:
            if y+y_shift not in rocks:
                rocks[y+y_shift] = set()
            rocks[y+y_shift].add(x+x_shift)
            min_height = max(min_height, y+y_shift+1)

        if len(rocks[min_height-1]) == 7:
            store.append([min_height-1, curr_form, j, i])
            rocks = {}
            rocks[min_height-1] = {0,1,2,3,4,5,6}


    # find cycle see what height we need to start at to get the remaining of our cycle
    # for second case we have remainder of 1675 so we need to calcualte up to 1675


    start_j = 1133
    start_i = 3670
    start_h = 5685
    repeat_i = 1735
    repeat_h = 2695

    total_i = 1000000000000-start_i
    total_c = total_i//repeat_i
    remaining_i = 1000000000000 - (start_i + total_c*repeat_i)
    
    print(min_height+start_h+total_c*repeat_h)
    
    

