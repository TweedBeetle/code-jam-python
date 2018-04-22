from IO import *
import numpy as np

# input_file_name = 'test input'
# input_file_name = 'B-small-practice.in'
input_file_name = 'B-large-practice.in'
file_contents = read_input(input_file_name, ['T'], ['S'], try_cast=False)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

def flip(stack, n):

    return ''.join('1' if x == '0' else '0' for x in stack[:n])[::-1] + stack[n:]

for inputs in case_inputs:

    s = inputs['S'].replace('+', '1').replace('-', '0')

    req_flips = np.abs(np.diff([int(v) for v in s])).sum()  # smooth af
    # if (req_flips % 2 == 0 and s[0] == '0') or (req_flips % 2 == 1 and s[0] == '1'):
    #     req_flips += 1
    req_flips += req_flips % 2 == int(s[0])
    outputs.append([req_flips])
    print ''

print outputs
write_list_of_lists(outputs)
