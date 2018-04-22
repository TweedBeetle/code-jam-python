def read_input_advanced(location, matcher_dict):

    with open(location) as f:
        all_lines = f.readlines()

    all_lines = [line.strip('\n') for line in all_lines]

    num_cases = int(all_lines[0])

    var_sequences_dict = {}

    def try_int(v):
        try:
            return int(v)
        except ValueError:
            return v

    for var_sequence, matcher in matcher_dict.items():
        var_sequences_dict[var_sequence] = [[try_int(v) for v in line.split(' ')] for line in all_lines[1:] if matcher(line)]

    var_dict = {'num_cases': num_cases}

    for var_sequence in matcher_dict.keys():
        if len(var_sequence) == 1:
            var_dict[var_sequence] = var_sequences_dict[var_sequence]
        else:
            for i, var in enumerate(var_sequence):
                var_dict[var] = [v[i] for v in var_sequences_dict[var_sequence]]

    return var_dict

def read_input(location, headers, inputs, try_cast=False):

    with open(location) as f:
        all_lines = f.readlines()

    all_lines = [line.strip('\n') for line in all_lines]
    # all_lines = [line for line in all_lines if not line.strip() == '']

    if try_cast:
        def cast(v):
            try:
                return int(v)
            except:
                return v
    else:
        cast = lambda v: v

    num_headers = len(headers)
    header_vars = {name: cast(value) for name, value in zip(headers, all_lines[:num_headers])}

    num_inputs = len(inputs)
    num_cases = (len(all_lines) - num_headers) / num_inputs

    case_inputs = []

    for i in range(num_cases):
        start_ind = num_headers + i * num_inputs
        stop_ind = num_headers + num_inputs + i * num_inputs
        case_input = {name: cast(value) for name, value in zip(inputs, all_lines[start_ind:stop_ind])}
        case_inputs.append(case_input)

    return header_vars, case_inputs

def list_to_writeable(l):

    return ' '.join([str(v) for v in l]) + '\n'

def write_list_of_lists(outputs, fname='output'):

    writeable_ouptut_list = case_prefix_output_strings([list_to_writeable(output) for output in outputs])
    write_list_to_file(writeable_ouptut_list, fname)

def case_prefix_output_strings(output_strings):

    prefixed_output_strings = []

    c = 1
    for output_string in output_strings:
        prefixed_output_string = 'Case #{}: '.format(c) + output_string
        prefixed_output_strings.append(prefixed_output_string)
        c += 1

    return prefixed_output_strings

def write_list_to_file(l, fname='output'):
    with open(fname, 'w') as f:
        for v in l:
            f.write(v)

def write(v, fname='output'):
    with open(fname, 'w') as f:
        f.write(v)