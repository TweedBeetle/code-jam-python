from IO import *
import numpy as np

input_file_name = 'A-large-practice.in'
with open(input_file_name) as f:
    all_lines = f.readlines()

all_lines = [line.strip('\n') for line in all_lines]

num_cases = int(all_lines[0])
N_K = [[int(v) for v in line.split(' ')] for line in all_lines[1:] if ' ' in line]
N = [nk[0] for nk in N_K]
K = [nk[1] for nk in N_K]

print N
print K

cases = []
outputs = []

for i in range(num_cases):

    start_ind = sum(N[:i]) + 2 + i
    stop_ind = start_ind + N[i]
    board_rows = all_lines[start_ind:stop_ind]
    board_rows = [list(row) for row in board_rows]
    board = np.array(board_rows)

    case = {
        'board': board,
        'k': K[i]
    }
    cases.append(case)

def apply_gravity_to_board(board):

    gravitised_board = board.copy()
    n = board.shape[0]
    for i in range(n):
        last_board = gravitised_board.copy()
        for y in range(n-1)[::-1]:
            for x in range(n):
                char = gravitised_board[y, x]
                # print (y, x), char
                if char != '.' and gravitised_board[y+1, x] == '.':
                    gravitised_board[y+1, x] = char
                    gravitised_board[y, x] = '.'
        if np.all(last_board == gravitised_board):
            break

    return gravitised_board

def has_won(board, symbol, k):
    n = board.shape[0]
    inds = np.argwhere(board == symbol).tolist()
    for y, x in inds:
        # down
        if y + k <= n:
            needed_inds = [[y+i, x] for i in range(k)]
            for needed_ind in needed_inds:
                if needed_ind not in inds:
                    break
            else:
                print (y, x), 'down'
                return True
        # right
        if x + k <= n:
            needed_inds = [[y, x+i] for i in range(k)]
            for needed_ind in needed_inds:
                if needed_ind not in inds:
                    break
            else:
                print (y, x), 'right'
                return True
        # down right
        if x + k <= n and y + k <= n:
            needed_inds = [[y+i, x+i] for i in range(k)]
            for needed_ind in needed_inds:
                if needed_ind not in inds:
                    break
            else:
                print (y, x), 'down right'
                return True
        # down left
        if x - k + 1 >= 0 and y + k <= n:
            needed_inds = [[y+i, x-i] for i in range(k)]
            for needed_ind in needed_inds:
                if needed_ind not in inds:
                    break
            else:
                print (y, x), 'down left'
                return True
    return False

for case in cases:

    k = case['k']

    rotated_board = np.rot90(case['board'], 3)
    rotated_gravitised_board = apply_gravity_to_board(rotated_board)
    print rotated_gravitised_board
    R_wins = has_won(rotated_gravitised_board, 'R', k)
    B_wins = has_won(rotated_gravitised_board, 'B', k)
    if R_wins and B_wins:
        outputs.append(['Both'])
    elif R_wins:
        outputs.append(['Red'])
    elif B_wins:
        outputs.append(['Blue'])
    else:
        outputs.append(['Neither'])

    print ''

write_list_of_lists(outputs)


