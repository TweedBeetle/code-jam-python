from IO import read_input, write_list_of_lists

input_file_name = 'B-large-practice.in'
file_contents = read_input(input_file_name, ['N'], ['W'], try_cast=False)

num_cases = file_contents[0]['N']
case_inputs = file_contents[1]

outputs = []

for inputs in case_inputs:
    W = inputs['W']

    outputs.append(W.split(' ')[::-1])

write_list_of_lists(outputs)
