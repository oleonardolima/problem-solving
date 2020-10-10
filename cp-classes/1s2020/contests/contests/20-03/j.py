num_stones = int(input())
stones = list(input())

num_stones_to_remove = 0
idx_i = 0
idx_j = 1
while idx_j < num_stones:
    if stones[idx_i] == stones[idx_j]:
        num_stones_to_remove += 1
    idx_i += 1
    idx_j += 1

print(num_stones_to_remove)