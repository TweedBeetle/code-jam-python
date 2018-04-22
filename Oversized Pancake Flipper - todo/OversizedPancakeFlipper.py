from IO import *
import numpy as np

# https://code.google.com/codejam/contest/3264486/dashboard#s=p0

# input_file_name = 'test input'
# input_file_name = 'B-small-practice.in'
# input_file_name = 'B-large-practice.in'
input_file_name = get_input_file_name()
file_contents = read_input(input_file_name, ['T'], ['SK'], try_cast=False)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

def flip(stack, n):

    return ''.join('1' if x == '0' else '0' for x in stack[:n]) + stack[n:]

for inputs in case_inputs:

    S = inputs['SK'].split(' ')[0]
    k = inputs['SK'].split(' ')[1]
    s = S.replace('+', '1').replace('-', '0')

    print s, k

    print ''

print outputs
write_list_of_lists(outputs)
