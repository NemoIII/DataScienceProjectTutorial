from collections import Counter

'''Reading Data'''
filename = '../TxtFiles/input.txt'

with open(filename) as fn:
    # Read each line
    line = fn.readline()

    # Keep count of lines
    line_count = 1
    while line:
        print('Line {}: {}'.format(line_count, line.strip()))
        line = fn.readline()
        line_count += 1


print('-_-_-_-_' * 20)

'''Counting Word Frequency'''

with open(r'../TxtFiles/input.txt') as f:
    p = Counter(f.read().split())
    print(p)
