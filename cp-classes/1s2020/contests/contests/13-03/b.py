import string

alphabet = list(string.ascii_lowercase)
t_queries = int(input())

for query in range(t_queries):
    input_ = input()
    input_ = list(input_.split(" "))

    n = int(input_[0])
    k = int(input_[-1])

    # new_str = [' ' for n in range(n)]
    new_str = []

    if n == k:
        for letter in range(k):
            new_str.append(alphabet[letter])
    else:
        # max_min_freq = n // k
        # hash_table = {}

        while len(new_str) < n:
            for letter in range(k):
                new_str.append(alphabet[letter])
                #hash_table[alphabet[letter]] = 1
                if len(new_str) >= n:
                    break

            if len(new_str) >= n:
                break

        # letter = 0
        # for element in range(k, n):
        #     if hash_table[alphabet[letter]] <= max_min_freq:
        #         hash_table[alphabet[letter]] += 1
        #         new_str[element] = alphabet[letter]
        #     else:
        #         while(hash_table[alphabet[letter]] >= max_min_freq and letter < k):
        #             letter += 1
        #         hash_table[alphabet[letter]] += 1
        #         new_str[element] = alphabet[letter]
                
        #         if (letter == k - 1) and (hash_table[alphabet[letter]] >= max_min_freq):
        #             for i in range(k):
        #                 hash_table[alphabet[i]] = 0
        #             letter = 0

    new_str = "".join(new_str)
    print(new_str)
    #print(len(new_str))