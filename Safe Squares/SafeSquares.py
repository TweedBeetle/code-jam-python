from IO import *
import numpy as np
from tqdm import tqdm

# input_file_name = 'test input'
# input_file_name = 'B-small-practice.in'
input_file_name = 'B-large-practice.in'


matcher_dict = {
    'RCK': lambda l: len(l.split(' ')) == 3,
    'YX': lambda l: len(l.split(' ')) == 2,
}

var_dict = read_input_advanced(input_file_name, matcher_dict)

outputs = []
case_inputs = []

for i in range(var_dict['num_cases']):

    input = {}

    Y = var_dict['Y']
    X = var_dict['X']
    K = var_dict['K']
    R = var_dict['R']
    C = var_dict['C']

    monster_coords_y = Y[sum(K[:i]): sum(K[:i+1])]
    monster_coords_x = X[sum(K[:i]): sum(K[:i+1])]

    monster_coords = zip(monster_coords_y, monster_coords_x)
    input['monster_coords'] = monster_coords

    input['R'] = R[i]
    input['C'] = C[i]
    input['K'] = K[i]

    case_inputs.append(input)

def extract_square_submatrices(m):

    submatrices = []

    for n in range(1, min(m.shape) + 1):
        for y in range(m.shape[0]):
            for x in range(m.shape[1]):
                if y + n > m.shape[0] or x + n > m.shape[1]:
                    continue
                submatrices.append(m[y:y+n, x:x+n])

    return submatrices

def count_safe_squares(m):

    bar = tqdm(total=min(m.shape) * m.shape[0] * m.shape[1], nested=True, leave=False)

    num_safe_squares = 0

    for n in range(1, min(m.shape) + 1):
        for y in range(m.shape[0]):
            for x in range(m.shape[1]):
                bar.update()
                if y + n > m.shape[0] or x + n > m.shape[1]:
                    continue
                if np.count_nonzero(m[y:y+n, x:x+n]) == 0:
                    num_safe_squares += 1
    return num_safe_squares

# for inputs in tqdm(case_inputs, leave=True):
#
#     print input
#
#     grid = np.zeros((inputs['R'], inputs['C']))
#     for coords in inputs['monster_coords']:
#         grid[coords[0], coords[1]] = 1
#
#     print grid
#
#     num_safe_squares = count_safe_squares(grid)
#     print num_safe_squares
#     print ''
#
#     outputs.append([num_safe_squares])

for inputs in tqdm(case_inputs, leave=True):

    grid = np.zeros((inputs['R'], inputs['C']))
    for coords in inputs['monster_coords']:
        grid[coords[0], coords[1]] = 1

    print grid

    if min(grid.shape) <= 2:
        num_safe_squares = count_safe_squares(grid)
    elif inputs['K'] == 0:
        if grid.shape[0] == grid.shape[1]:
            num_safe_squares = sum([x**2 for x in range(1, grid.shape[0] + 1)])
        else:
            assert False
    else:
        safe_points = np.argwhere(grid == 0).tolist()
        safe_points_set = set([tuple(safe_point) for safe_point in safe_points])
        num_safe_squares = len(safe_points)

        square_tree = {1: safe_points}

        for i in tqdm(range(2, min(grid.shape) + 1), nested=True, leave=False):
            square_tree[i] = []
            # print i
            adders = []
            for y in range(i):
                adders.append(np.array([y, i-1]))
            for x in range(i - 1):
                adders.append(np.array([i-1, x]))
            for square in tqdm(square_tree[i - 1], nested=True):
                # print ''
                needed_points = [square + adder for adder in adders]
                needed_points = [tuple(point) for point in needed_points]

                # print square
                # print needed_points
                for needed_point in needed_points:
                    # if needed_point not in safe_points_set:
                    # print needed_point
                    try:
                        if grid[needed_point[0], needed_point[1]] == 1:
                            # print needed_point
                            break
                    except IndexError:
                        break
                else:
                    # print 'safe'
                    square_tree[i].append(square)
            num_safe_squares += len(square_tree[i])

    print num_safe_squares
    outputs.append([num_safe_squares])
    print ''

write_list_of_lists(outputs)
