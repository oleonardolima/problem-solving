input_ = [int(element) for element in input().split(" ")]
# print(input_)
n = input_[0]
acceptable_lengths = input_[1:]
#print(n)
#print(acceptable_lengths)
acceptable_lengths.sort()
max_possible_pieces = n // acceptable_lengths[0]
print(max_possible_pieces)