from IO import *
import numpy as np

input_file_name = 'A-large-practice.in'

with open(input_file_name) as f:
    all_lines = f.readlines()

all_lines = [line.strip('\n') for line in all_lines]

num_cases = int(all_lines[0])

def is_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

# num_names = [int(line) for line in all_lines[1:] if is_int(line)]
num_names = [int(line) for line in all_lines[1:] if line.isdigit()]  # isdigit not tested
cases = []

outputs = []

for i in range(num_cases):
    start_ind = sum(num_names[:i]) + 2 + i
    stop_ind = start_ind + num_names[i]
    names = all_lines[start_ind:stop_ind]
    cases.append(names)

for names in cases:

    num_unique_letters = []
    for name in names:
        letter_set = set(name)
        if ' ' in letter_set:
            letter_set.remove(' ')
        num_unique_letters.append(len(letter_set))

    num_unique_letters = np.array(num_unique_letters)
    most_unique_letters = max(num_unique_letters)

    inds = np.where(num_unique_letters == most_unique_letters)
    if len(inds[0]) > 1:
        possible_winners = np.array(names)[inds]
        winner = sorted(possible_winners)[0]
    else:
        winner = np.array(names)[inds][0]

    outputs.append([winner])

write_list_of_lists(outputs)
