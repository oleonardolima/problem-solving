watermelon_weight = int(input())
if watermelon_weight > 0:
    if watermelon_weight > 2 and watermelon_weight % 2 == 0:
        print ("YES")
    else:
        print("NO")
        # isPossible = False
        # pete_part_weight = 0
        # billy_part_weight = 0
        # while watermelon_weight > 0:
        #     if pete_part_weight % 2 == 0 and billy_part_weight % 2 == 0 and watermelon_weight % 2 == 0:
        #         isPossible = True
        #         break
        #     pete_part_weight += 1
        #     billy_part_weight += 2

        #     watermelon_weight -= 1
        #     if watermelon_weight - 1 > 0:
        #         watermelon_weight -= 1
        #     else:
        #         break
else:
    print("NO")
