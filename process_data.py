import os

def read_all_lines(filename, encoding='utf8'):
    with open(filename, encoding=encoding) as file:
        for line in file:
            line = line.rstrip().strip('\ufeff')
            if line:
                yield line


def write_all_lines(filename, lines, encoding='utf8'):
    with open(filename, 'w', encoding=encoding) as file:
        for line in lines:
            file.write(line + '\n')


def process_file(filename, src_name, tgt_name):
    q = None
    a = None
    questions = []
    answers = []
    for line in read_all_lines(filename):
        if line == '<P>':
            questions.append(q)
            answers.append(a)
            a = q = None
        elif a is None:
            a = ' '.join(line)
        else:
            q = ' '.join(line)
    write_all_lines(src_name, answers)
    write_all_lines(tgt_name, questions)


process_file('./data/train.txt', './data/src-train.txt', './data/tgt-train.txt')
process_file('./data/dev.txt', './data/src-val.txt', './data/tgt-val.txt')