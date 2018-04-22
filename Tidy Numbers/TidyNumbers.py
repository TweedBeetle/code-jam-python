from IO import *
import numpy as np

input_file_name = get_input_file_name()
# input_file_name = 'B-large.in'
# input_file_name = 'A-small-practice.in'
# input_file_name = 'A-large-practice.in'
print input_file_name
file_contents = read_input(input_file_name, ['T'], ['N'], try_cast=True)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

def is_tidy(x):

    s = str(x)

    if len(s) == 1:
        return True

    a = np.array([int(v) for v in s])
    d = np.diff(a)

    return np.all(d >= 0)

for inputs in case_inputs:

    n = inputs['N']
    # n = 34543

    print n

    # for x in xrange(n, 0, -1):
    #     if is_tidy(x):
    #         print x
    #         outputs.append([x])
    #         break

    x = n

    while not is_tidy(x):
        d = np.diff(np.array([int(v) for v in str(x)]))
        print d
        i = np.argwhere(d < 0)[0][0] + 1
        print i
        print int(str(x)[i:]) - 1
        x = x - int(str(x)[i:]) - 1

    print x
    outputs.append([x])

    print ''

write_list_of_lists(outputs)
