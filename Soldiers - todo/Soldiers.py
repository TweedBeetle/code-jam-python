from IO import *
import numpy as np

# https://code.google.com/codejam/contest/6274486/dashboard#s=p3

input_file_name = 'test input'
# input_file_name = 'A-small-practice.in'
# input_file_name = 'A-large-practice.in'

matcher_dict = {
    'N': lambda l: ' ' not in l,
    'AD': lambda l: ' ' in l,
}

var_dict = read_input_advanced(input_file_name, matcher_dict)
var_dict['N'] = [v[0] for v in var_dict['N']]
# print var_dict
outputs = []
case_inputs = []

for i in range(var_dict['num_cases']):

    input = {}

    N = var_dict['N']
    A = var_dict['A']
    D = var_dict['D']

    attack_stats = A[sum(N[:i]): sum(N[:i+1])]
    defence_stats = D[sum(N[:i]): sum(N[:i+1])]
    soldier_stats = zip(attack_stats, defence_stats)

    input['num_soldiers'] = N[i]
    input['soldier_stats'] = soldier_stats

    case_inputs.append(input)

outputs = []

def is_pickable_gen(max_a, max_d):
    def is_pickable(stats):
        return stats[0] > max_a or stats[1] > max_d
    return is_pickable

for input in case_inputs[:1]:

    print input

    soldier_stats = np.array(input['soldier_stats'])

    if soldier_stats.shape[0] == 1:
        outputs.append(["YES"])
        continue

    max_a = 0
    max_d = 0

    print len(soldier_stats)
    soldier_stats = filter(is_pickable_gen(max_a, max_d), soldier_stats)
    print len(soldier_stats)

    pass

write_list_of_lists(outputs)
