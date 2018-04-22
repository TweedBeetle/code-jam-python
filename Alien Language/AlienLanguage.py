from IO import *
from collections import defaultdict
from tqdm import tqdm

input_file_name = 'A-large-practice.in'
# input_file_name = 'A-small-practice.in'
file_contents = read_input(input_file_name, ['LDN'], ['word'], try_cast=False)

length, num_known, num_unknown = [int(v) for v in file_contents[0]['LDN'].split(' ')]

known_words = [v['word'] for v in file_contents[1][:num_known]]
unknown_words = [v['word'] for v in file_contents[1][num_known:]]

print known_words
print unknown_words

def split_unknown_word(word):

    split_word = []

    i = 0
    while i < len(word):
        char = word[i]
        if char != '(':
            split_word.append([char])
            i += 1
        else:
            possibilities = []
            i += 1
            while word[i] != ')':
                possibilities.append(word[i])
                i += 1
            split_word.append(possibilities)
            i += 1

    return split_word


def build_known_word_tree(known_words):

    make_dict = lambda: defaultdict(make_dict)
    tree = make_dict()

    for word in known_words:
        node = tree
        for char in word:
            node = node[char]

    return tree

def build_possible_word_list(split_word):

    if len(split_word) != length:
        return []

    unknown_word_list = split_word[0]
    unknown_word_list = [word for word in unknown_word_list if word_in_tree(word, known_word_tree)]

    for options in split_word[1:]:
        expanded_word_list = [0] * (len(unknown_word_list) * len(options))
        c = 0
        for char in options:
            for word in unknown_word_list:
                expanded_word = word + char
                if word_in_tree(expanded_word, known_word_tree):
                    expanded_word_list[c] = expanded_word
                    c += 1
        unknown_word_list = [word for word in expanded_word_list if word != 0]

    return unknown_word_list

def num_possible_words(split_word):

    return len(build_possible_word_list(split_word))

def word_in_tree(word, tree):

    node = tree
    for char in word:
        if char in node.keys():
            node = node[char]
        else:
            return False
    else:
        return True

outputs = []
known_word_tree = build_known_word_tree(known_words)
split_words = [split_unknown_word(unknown_word) for unknown_word in unknown_words]

for split_word in tqdm(split_words):
    num_known_words = num_possible_words(split_word)
    outputs.append([num_known_words])


print outputs
write_list_of_lists(outputs)