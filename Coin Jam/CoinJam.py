from IO import *
import pyprimes
import primefac

input_file_name = get_input_file_name()
# input_file_name = 'test input'
# input_file_name = 'C-small-practice.in'
# input_file_name = 'C-large-practice.in'
print input_file_name
file_contents = read_input(input_file_name, ['T'], ['NJ'], try_cast=False)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

def interpret_as_base_i(n, i):
    if isinstance(n, int):
        n = str(n)
    return int(sum([long(v) * i ** x for v, x in zip(n, range(len(n))[::-1])]))

def find_factor(n):

    # for i in xrange(2, n):
    # i = 1.
    # while True:
    #     i += 1
    #     if n % i == 0:
    #         return i
    #     assert i <= n

    # return pyprimes.factorise(n).next()[0]
    return primefac.multifactor(n)

def sanity_check(jamcoin_dict):

    assert len(set(jamcoin_dict.keys())) == len(jamcoin_dict.keys())
    for jamcoin, divisors in jamcoin_dict.iteritems():
        assert len(divisors) == 9
        for i, divisor in enumerate(divisors):
            decimal_repr = interpret_as_base_i(jamcoin, i+2)
            assert decimal_repr % float(divisor) == 0
            assert divisor != decimal_repr
            assert divisor != 1

for inputs in case_inputs:

    print inputs
    n = int(inputs['NJ'].split(' ')[0])
    j = int(inputs['NJ'].split(' ')[1])
    print n, j

    valid_jamcoins = {}

    for i in xrange(2 ** (n - 2)):
        jamcoin = '1{}1'.format(bin(i)[2:].rjust(n-2, '0'))
        print jamcoin
        divisors = []
        for base in range(2, 11):
            decimal = interpret_as_base_i(jamcoin, base)
            if pyprimes.isprime(decimal):
                print 'p: {}'.format(decimal)
                break
            else:
                print base, decimal
                divisors.append(find_factor(decimal))
        else:
            valid_jamcoins[jamcoin] = divisors
        if len(valid_jamcoins) == j:
            break
        print ''

    print valid_jamcoins
    # sanity_check(valid_jamcoins)

lines = []

for jamcoin, divisors in valid_jamcoins.iteritems():
    line = [jamcoin]
    for divisor in divisors:
        line.append(str(divisor))
    lines.append(line)

for i in range(j):
    lines[i][0] = '\no_prefix' + lines[i][0]
print lines
outputs.append([''])
for line in lines:
    outputs.append(line)

print len(valid_jamcoins)
write_list_of_lists(outputs)
