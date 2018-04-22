from IO import *

input_file_name = 'A-large-practice.in'

with open(input_file_name) as f:
    all_lines = f.readlines()

all_lines = [line.strip('\n') for line in all_lines]

num_cases = int(all_lines[0])
num_wires = [int(line) for line in all_lines[1:] if ' ' not in line]

cases = []
outputs = []

for i in range(num_cases):
    wires = []
    start_ind = sum(num_wires[:i]) + 2 + i
    stop_ind = start_ind + num_wires[i]
    windows = all_lines[start_ind:stop_ind]
    windows = [tuple([int(v) for v in window.split(' ')]) for window in windows]
    cases.append(windows)

for windows in cases:
    num_intersections = 0
    for w1 in windows:
        for w2 in windows:
            if (w1[0] < w2[0] and w1[1] > w2[1]) or (w1[0] > w2[0] and w1[1] < w2[1]):
                num_intersections += 1
    num_intersections /= 2
    outputs.append([num_intersections])

write_list_of_lists(outputs)
