num_letters = int(input())
word_given = list(input())

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

consecutive_vowels = 0
idx_i = 0
idx_j = 1
#print(word_given)
while idx_j < num_letters:
    #print(word_given[idx_i:idx_j+1])
    if word_given[idx_i] in vowels and word_given[idx_j] in vowels:
        #print("#")
        num_letters -= 1
        current_idx = idx_j
        while current_idx < num_letters:
            #print(word_given[current_idx])
            #print(word_given[current_idx+1])
            word_given[current_idx] = word_given[current_idx + 1]
            #print(word_given)
            current_idx += 1
    else:
        idx_i += 1
        idx_j += 1
#print(word_given)
#print(num_letters)
print("".join(word_given[:num_letters]))