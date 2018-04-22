from IO import *
import numpy as np
from collections import defaultdict
from pprint import pprint
from copy import deepcopy

# input_file_name = 'test input'
# input_file_name = 'A-small-practice.in'
input_file_name = 'A-large-practice.in'

with open(input_file_name) as f:
    all_lines = f.readlines()

all_lines = [line.strip('\n') for line in all_lines]

def numbers_in_line(line):

    return any([str(i) in line for i in range(10)])

num_cases = int(all_lines[0])
RCXYS = [[int(v) for v in line.split(' ')] for line in all_lines[1:] if numbers_in_line(line) and len(line.split(' ')) == 5]
PQ = [[float(v) for v in line.split(' ')] for line in all_lines[1:] if numbers_in_line(line) and len(line.split(' ')) == 2]

R = [v[0] for v in RCXYS]
C = [v[1] for v in RCXYS]
Y = [v[2] for v in RCXYS]
X = [v[3] for v in RCXYS]
S = [v[4] for v in RCXYS]

P = [float(v[0]) for v in PQ]
Q = [float(v[1]) for v in PQ]

# print RCXYS
# print PQ

case_inputs = []
outputs = []

for i in range(num_cases):

    start_ind = sum(R[:i]) + ((i + 1) * 2) + 1
    stop_ind = start_ind + R[i]
    grid_rows = all_lines[start_ind:stop_ind]
    grid_rows = [list(row.replace(' ', '')) for row in grid_rows]
    grid = np.array(grid_rows)

    input = {
        'grid': grid,
        'steps': S[i],
        'p': P[i],
        'q': Q[i],
        'start_x': X[i],
        'start_y': Y[i],
    }

    case_inputs.append(input)

class GameState:
    def __init__(self, grid, x, y, s, p, q, loaction_history=None, n=0, past_moves=None, a_hist=None):

        self.grid = grid
        self.x = x
        self.y = y
        self.s = s
        self.p = p
        self.q = q
        self.n = n

        if loaction_history is None:
            self.loaction_history = defaultdict(lambda: 0)
        else:
            self.loaction_history = loaction_history

        if past_moves is None:
            self.past_moves = [(y, x)]
        else:
            self.past_moves = past_moves

        if a_hist is None:
            self.a_hist = [0]
        else:
            self.a_hist = a_hist

    def show(self):

        grid_representation = self.grid.copy()
        grid_representation[self.y, self.x] = 'P'
        print grid_representation
        pprint(dict(
            yx=(self.y, self.x),
            s=self.s,
            n=self.n,
            p=self.p,
            q=self.q,
            loaction_history=self.loaction_history,
            past_moves=self.past_moves,
            a_hist=self.a_hist,
        ))

    def copy(self):

        return deepcopy(self)

    def has_attractor(self, move):

        return self.grid[move[0], move[1]] == 'A'

    def possible_moves(self):

        moves = []

        if self.x < self.grid.shape[1] - 1:
            moves.append((self.x + 1, self.y))
        if self.x > 0:
            moves.append((self.x - 1, self.y))
        if self.y < self.grid.shape[0] - 1:
            moves.append((self.x, self.y + 1))
        if self.y > 0:
            moves.append((self.x, self.y - 1))

        moves = [m[::-1] for m in moves]

        return moves

    def make_move(self, move):

        new_game_state = self.copy()
        prob = (self.p if self.has_attractor(move) else self.q)

        if self.loaction_history[move] == 0:
            a = prob
        else:
            a = prob * (1 - prob) ** self.loaction_history[move]

        new_game_state.n += a

        new_game_state.loaction_history[move] += 1

        new_game_state.s -= 1

        new_game_state.y = move[0]
        new_game_state.x = move[1]

        new_game_state.past_moves = self.past_moves + [move]
        new_game_state.a_hist = self.a_hist + [a]

        return new_game_state

    def create_child_game_states(self):

        moves = self.possible_moves()

        child_game_states = []

        for move in moves:

            new_game_state = self.make_move(move)
            child_game_states.append(new_game_state)

        return child_game_states

flatten_list_of_lists = lambda ll: [v for l in ll for v in l]

for input in case_inputs:

    if input['steps'] == 0 or input['grid'].shape == (1, 1):
        outputs.append([0])
        continue

    game_state = GameState(
        grid=input['grid'],
        x=input['start_x'],
        y=input['start_y'],
        s=input['steps'],
        p=input['p'],
        q=input['q'],
    )

    new_game_states = [game_state]

    # game_state.show()

    for i in range(input['steps']):
        new_game_states = [game_state.create_child_game_states() for game_state in new_game_states]
        new_game_states = flatten_list_of_lists(new_game_states)

    expected_monsters = max([game_state.n for game_state in new_game_states])

    best_game_state = sorted(new_game_states, key=lambda s: s.n, reverse=True)[0]
    best_game_state.show()

    print len(new_game_states)
    print expected_monsters
    print ''

    outputs.append([expected_monsters])

write_list_of_lists(outputs)
