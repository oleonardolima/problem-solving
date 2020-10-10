sequence = list(input())
#print(sequence)
num_queries = int(input())

for query in range(num_queries):
    input_indexes = list(input().split(" "))
    left_index = int(input_indexes[0]) - 1
    right_index = int(input_indexes[-1]) - 1

    num_correct_brackets = 0
    char_stack = []
    while left_index <= right_index:
        if sequence[right_index] == "(":
            if len(char_stack) > 0:
                char_stack.pop()
                num_correct_brackets += 2
        else:
            char_stack.append(sequence[right_index])
        right_index -= 1
    print(num_correct_brackets)