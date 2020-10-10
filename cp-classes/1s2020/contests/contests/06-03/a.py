input = list(input().split(" "))
n = int(input[0])
k = int(input[-1])

origami = [2, 5, 8]
n_notebooks = []

total = 0
for color in origami:
   total += -(-color*n // k)

print(total)
