from IO import *

# input_file_name = 'test input'
# input_file_name = 'C-small-practice.in'
input_file_name = 'C-large-practice.in'

matcher_dict = {
    'N': lambda l: '(' not in l,
    'E': lambda l: '(' in l,
}

var_dict = read_input_advanced(input_file_name, matcher_dict)
var_dict['N'] = [v[0] for v in var_dict['N']]
var_dict['E'] = [v[0] for v in var_dict['E']]
# print var_dict
outputs = []
case_inputs = []

for i in range(var_dict['num_cases']):

    input = {}

    N = var_dict['N']
    E = var_dict['E']

    input['expressions'] = E[sum(N[:i]): sum(N[:i+1])]
    input['num_expressions'] = N[i]

    case_inputs.append(input)

# print case_inputs

for inputs in case_inputs:

    evaluated = set()
    map = dict()

    for expression in inputs['expressions']:
        split_expression = expression.split('=')
        given = split_expression[0]
        needed = split_expression[1][split_expression[1].find('('):].replace('(', '').replace(')', '').split(',')
        # forgive me. This is code jam not a f500
        if needed == ['']:
            needed = []
        map[given] = needed

    print map

    status = 'GOOD'

    while len(evaluated) != len(map):
        for given, needed in map.iteritems():
            if given not in evaluated and (len(needed) == 0 or all([n in evaluated for n in needed])):
                evaluated.add(given)
                break
        else:
            status = 'BAD'
            break

    print evaluated
    print status
    print ''

    outputs.append([status])

write_list_of_lists(outputs)
