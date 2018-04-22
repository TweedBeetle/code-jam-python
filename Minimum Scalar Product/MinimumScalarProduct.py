from IO import *
import numpy as np

input_file_name = 'A-large-practice.in'
file_contents = read_input(input_file_name, ['T'], ['n', 'v1', 'v2'], try_cast=False)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

for inputs in case_inputs:
    x = inputs['v1']
    y = inputs['v2']

    x = np.array([int(v) for v in x.split(' ')])
    y = np.array([int(v) for v in y.split(' ')])

    minimum_scalar_product = np.dot(sorted(x), sorted(y, reverse=True))

    outputs.append([minimum_scalar_product])

# print outputs
write_list_of_lists(outputs)