from collections import defaultdict
from IO import write_list_of_lists

input_file_name = 'A-large-practice.in'

with open(input_file_name) as f:
    all_lines = f.readlines()

all_lines = [line.strip('\n') for line in all_lines]

num_cases = int(all_lines[0])
num_given_needed = [[int(v) for v in line.split(' ')] for line in all_lines[1:] if '/' not in line]

print num_given_needed

cases = []
outputs = []

for i in range(num_cases):

    given_start_ind = sum([v for l in num_given_needed[:i] for v in l]) + 2 + i
    given_stop_ind = given_start_ind + num_given_needed[i][0]
    needed_stop_ind = given_stop_ind + num_given_needed[i][1]
    case = {
        'given_dirs': all_lines[given_start_ind:given_stop_ind],
        'needed_dirs': all_lines[given_stop_ind:needed_stop_ind]
    }
    print case
    cases.append(case)


def build_dir_tree(dirs):

    make_dict = lambda: defaultdict(make_dict)
    tree = make_dict()

    for dir in dirs:
        node = tree
        for name in dir:
            node = node[name]

    return tree

def num_dirs_not_in_tree(dirs, tree):

    n = 0

    for dir in dirs:
        node = tree
        for name in dir:
            if name in node.keys():
                node = node[name]
            else:
                n += 1
                node = node[name]

    return n

for case in cases:

    given_dirs = [given_dir.split('/')[1:] for given_dir in case['given_dirs']]
    given_dir_tree = build_dir_tree(given_dirs)
    # print given_dir_tree

    needed_dirs = [needed_dir.split('/')[1:] for needed_dir in case['needed_dirs']]

    num_commands = num_dirs_not_in_tree(needed_dirs, given_dir_tree)
    # print num_commands

    outputs.append([num_commands])

print outputs
write_list_of_lists(outputs)