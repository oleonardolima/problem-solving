from sys import stdin

for input_line in stdin:
    if input_line == '\n':
        break
    # print(input_line)
    alphabet_range = int(input_line[0])
    word_length = int(input_line[-1])

    num_words = 0
    print("{:.5f}".format(num_words / alphabet_range))