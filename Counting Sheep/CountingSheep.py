from IO import *

# input_file_name = 'test input'
# input_file_name = 'A-small-practice.in'
input_file_name = 'A-large-practice.in'
file_contents = read_input(input_file_name, ['T'], ['N'], try_cast=True)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

for inputs in case_inputs:

    n = inputs['N']
    print n

    if n == 0:
        outputs.append(['INSOMNIA'])
        continue

    seen_digits = set(str(n))

    i = 0
    x = n
    while len(seen_digits) != 10:
        i += 1
        x = n * i
        for digit in str(x):
            seen_digits.add(digit)

    outputs.append([x])
    print x
    print ''

print outputs

write_list_of_lists(outputs)
