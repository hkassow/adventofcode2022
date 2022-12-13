
'ax rock'
'by paper'
'cz scissor'
#part 1 first input is what they choose second input is what you choose
#part 2 first input is what they choose second input is the outcome of the game
shape_score = {'X':1, 'Y':2, 'Z':3}
outcome_score = {'AX':3, 'AY':6, 'AZ':0, "BY":3, 'BZ':6, 'BX':0, 'CZ':3, 'CX':6, 'CY':0}

outcome_score2 = {'X':0, 'Y':3, 'Z':6}
shape_score2 = {'AX':3, 'AY':1, 'AZ':2, 'BX':1, 'BY':2, 'BZ':3, 'CX':2, 'CY':3, 'CZ':1 }

with open('input_day2.txt') as f:
    lines = f.readlines()
    res = 0
    res2 = 0
    for line in lines:
        res += shape_score[line[2]] + outcome_score[line[0]+line[2]]
        res2 += outcome_score2[line[2]] + shape_score2[line[0] + line[2]]
    print(res,res2)