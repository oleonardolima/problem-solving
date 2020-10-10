string_length = int(input())
input_string = list(input())

#print(input_string)

letters_to_remove = 0
idx_i = 0
idx_j = 2
while idx_i < string_length:
    current_substring = "".join(input_string[idx_i:idx_j+1])
    #print(current_substring)
    if current_substring == 'xxx':
        letters_to_remove += 1
        #print(letters_to_remove)
    idx_i += 1
    idx_j += 1

print(letters_to_remove)