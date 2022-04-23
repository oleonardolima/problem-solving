input_ = input().split(" ")
n_parts = int(input_[0])
m_ropes = int(input_[-1])

energy_values = [int(el) for el in input().split(" ")]
print(energy_values)
parts = {}
for idx in range(n_parts):
   parts[idx] = [[], 0, False]
print(parts)
for i in range(m_ropes):
    input_ = input().split(" ")
    print(input_)
    x = int(input_[0])
    y = int(input_[-1])

    parts[x - 1][0].append(y - 1)
    parts[x - 1][1] += energy_values[y - 1]
    
    parts[y - 1][0].append(x - 1)
    parts[y - 1][1] += energy_values[x - 1]

    #parts.sort(key = lambda x: x[2])
    print(parts)
    total_cost = 0
#     print(parts)
# def total_cost(complete_cost, curr_cost, total_cost):
#     if curr_cost[3]:
#         return 0
#     else:
#         total_cost += curr_cost[2]
#         curr_cost[3] = True
#         for c in curr_cost[1]:
#             total_cost += total_cost(complete_cost, complete_cost[])
#         return total_cost
#     print(cost)