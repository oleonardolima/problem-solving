string_length = int(input())
input_string = list(input())

two_gram_dict = {}

idx_i = 0
idx_j = 1
while idx_j < string_length:
    two_gram_key = "".join(input_string[idx_i:idx_j+1])
    if two_gram_key not in two_gram_dict:
        two_gram_dict[two_gram_key] = 1
    else:
        two_gram_dict[two_gram_key] += 1
    #print(two_gram_key)
    idx_i += 1
    idx_j += 1

#print("!!!!")

maximal_two_grams = ""
maximal_count = 0
for key in two_gram_dict:
    if two_gram_dict[key] > maximal_count:
        maximal_two_grams = key
        maximal_count = two_gram_dict[key]
    #print(key)
    #print(two_gram_dict[key])

#print("!!!!")
print(maximal_two_grams)