from IO import *
import string

input_file_name = 'C-large-practice.in'
file_contents = read_input(input_file_name, ['N'], ['M'], try_cast=False)

num_cases = file_contents[0]['N']
case_inputs = file_contents[1]

abc = string.ascii_lowercase

num_letter_mapping = {
    2:abc[:3],
    3:abc[3:6],
    4:abc[6:9],
    5:abc[9:12],
    6:abc[12:15],
    7:abc[15:19],
    8:abc[19:22],
    9:abc[22:],
}

# pprint(num_letter_mapping)

letter_num_mapping = {}

for char in abc:
    for key, val in num_letter_mapping.items():
        if char in val:
            index = val.index(char)
            mapping = {'num': key, 'reps': index+1}
            break
    letter_num_mapping[char] = mapping

letter_num_mapping[' '] = {'num': 0, 'reps': 1}

# pprint(letter_num_mapping)

outputs = []

for inputs in case_inputs:
    message = inputs['M']

    output = ''
    last_num = None

    for char in message:
        char_map = letter_num_mapping[char]
        if str(char_map['num']) == last_num:
            output += ' '
        output += str(char_map['num']) * char_map['reps']

        last_num = output[-1]

    outputs.append([output])

write_list_of_lists(outputs)