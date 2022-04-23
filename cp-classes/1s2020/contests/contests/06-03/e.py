input_ = input()
input_ = list(input_.split(" "))
n = int(input_[0])
m = int(input_[-1])

print(n)
print(m)
table = []
for line in range(n):
    row = input()
    table.append(row)
print(table)
