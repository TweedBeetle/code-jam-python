from IO import *
import numpy as np
np.random.seed(1337)

input_file_name = get_input_file_name()
# input_file_name = 'test input'
# input_file_name = 'A-small-practice.in'
# input_file_name = 'A-large-practice.in'
print input_file_name

matcher_dict = {
    'RC': lambda l: ' ' in l,
    'l': lambda l: ' ' not in l,
}

var_dict = read_input_advanced(input_file_name, matcher_dict)

case_inputs = []

for i in range(var_dict['num_cases']):

    input = {}

    R = var_dict['R']
    C = var_dict['C']

    input['R'] = var_dict['R'][i]
    input['C'] = var_dict['C'][i]

    input['grid'] = var_dict['l'][sum(R[:i]): sum(R[:i+1])]
    input['grid'] = np.array([np.array(list(l[0])) for l in input['grid']])

    case_inputs.append(input)

outputs = []

def random_expand(grid):

    chars = filter(lambda c: c != '?', np.unique(grid))

    while '?' in grid:

        d = {char: {'right': None, 'left': None, 'up': None, 'down': None} for char in chars}

        for char in chars:

            print char
            coords = np.argwhere(grid == char)[0]

            right = 0
            while True:
                right += 1
                try:
                    if grid[tuple(coords + [0, right])] != '?':
                        break
                except IndexError as e:
                    break
            right -= 1

            left = 0
            while True:
                left += 1
                try:
                    if grid[tuple(coords + [0, -left])] != '?':
                        break
                except IndexError as e:
                    break
            left -= 1

            down = 0
            while True:
                down += 1
                try:
                    if grid[tuple(coords + [down, 0])] != '?':
                        break
                except IndexError as e:
                    break
            down -= 1

            up = 0
            while True:
                up += 1
                try:
                    if grid[tuple(coords + [-up, up])] != '?':
                        break
                except IndexError as e:
                    break
            up -= 1

            print right, left, down, up

            d[char]['right'] = right
            d[char]['left'] = left
            d[char]['down'] = down
            d[char]['up'] = up
            d[char]['coords'] = coords

        char = np.random.choice(chars)

        coords = d[char]['coords']
        print char
        print d[char]

        if np.random.choice([0, 1]) == 0:
            right = d[char]['right']
            left = d[char]['left']
            grid[coords[0], coords[1] - left: coords[1] + right + 1] = char
        else:
            up = d[char]['up']
            down = d[char]['down']
            grid[coords[0] - up: coords[1] + down + 1, coords[1]] = char

        print grid

for inputs in case_inputs:

    print inputs

    grid = inputs['grid']

    grid = random_expand(grid)
    print grid

    outputs.append([])

write_list_of_lists(outputs)
