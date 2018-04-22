from IO import *

input_file_name = 'A-large-practice.in'
file_contents = read_input(input_file_name, ['T'], ['S'], try_cast=False)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

print case_inputs

outputs = []

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

for inputs in case_inputs:

    # symbols = str(inputs['S'])
    symbols = inputs['S']
    unique_symbols = unique(symbols)
    base = len(unique_symbols)
    base = max(base, 2)

    map = {s: None for s in symbols}

    map[unique_symbols[0]] = 1
    if len(unique_symbols) > 1:
        map[unique_symbols[1]] = 0
    if len(unique_symbols) > 2:
        p = 2
        for symbol in symbols:
            if map[symbol] is None:
                map[symbol] = p
                p += 1

    # p = 1
    # for symbol in symbols:
    #     if map[symbol] is None:
    #         map[symbol] = p
    #         p += 1

    time = 0

    for p, symbol in zip(range(len(symbols))[::-1], symbols):
        # print type(symbol)
        time += map[str(symbol)] * base ** p

    print symbols
    print map
    print unique_symbols
    print time
    print ''
    outputs.append([time])

write_list_of_lists(outputs)
