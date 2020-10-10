from collections import defaultdict
len_str = int(input())
input_str = [char for char in input()]

# print(input_str)
letters_freq = defaultdict(int)

for letter in input_str:
    letters_freq[letter] += 1

# print(letters_freq)

num_ones = letters_freq['n']
num_zeros = letters_freq['z']

for i in range(num_ones):
    print(1, end=" ")
for i in range(num_zeros):
    print(0, end=" ")