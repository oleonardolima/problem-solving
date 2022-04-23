_input = [int(num) for num in input().split(" ")]
num_items = _input[0]
minimum_cost = _input[1]

items_price = [int(price) for price in input().split(" ")]
items_price.sort()

ptr1 = 0
ptr2 = 1
winner_items = []
while ptr2 < num_items:
    if items_price[ptr1] + items_price[ptr2] > minimum_cost:
        winner_items.append(items_price[ptr1])
    else:
        if winner_items:
            if items_price[ptr1] + winner_items[-1] > minimum_cost:
                winner_items.append(items_price[ptr1])
    ptr1 += 1
    ptr2 += 1

max_num_items = num_items - len(winner_items)
print(max_num_items)