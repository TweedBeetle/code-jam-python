from IO import *
import numpy as np

# input_file_name = 'test input'
# input_file_name = 'A-small-practice.in'
input_file_name = 'A-large-practice.in'
file_contents = read_input(input_file_name, ['T'], ['W'], try_cast=False)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

for inputs in case_inputs:

    word = inputs['W']
    print word

    if len(word) == 1:
        outputs.append([1])
        continue

    tree_branches = []

    for i in range(len(word)):
        if i == 0:
            section = word[:2]
        elif i == len(word) - 1:
            section = word[-2:]
        else:
            section = word[i-1:i+2]
        num_unique_letters = len(set(section))
        tree_branches.append(float(num_unique_letters))

    # num_acceptable_answers = np.prod(tree_branches)

    prod = 1
    for k in tree_branches:
        prod = (prod * int(k)) % 1000000007

    outputs.append([prod])

write_list_of_lists(outputs)
