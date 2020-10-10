n_flats = int(input())
lights = [[int(light), False] for light in input().split(" ")]

idx_i = 0
idx_j = 2

n_pair = 0
while idx_j <= n_flats - 1:
    if lights[idx_i][0] == 1 and lights[idx_j][0] == 1 and lights[idx_i + 1][0] == 0:
        if not lights[idx_i][1] and not lights[idx_j][1]:
            lights[idx_i][1], lights[idx_j][1]  = True, True
            n_pair += 1
        #print(idx_j)
    idx_i += 1
    idx_j += 1
    #print(lights)

print(n_pair)