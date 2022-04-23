num_queries = int(input())
for _ in range(num_queries):
    candies = [int(num_candy) for num_candy in input().split(" ")]
    candies.sort()
    red_candies, green_candies, blue_candies = candies[0], candies[1], candies[2]

    max_days = 0

    if blue_candies >= red_candies + green_candies:
        num_days = 0
        num_days += red_candies
        red_candies -= red_candies
        blue_candies -= red_candies
        
        num_days += green_candies
        green_candies -= green_candies
        blue_candies -= green_candies

        max_days = max(max_days, num_days)
    else:
        num_days = 0
        if green_candies < blue_candies:
            num_days += blue_candies - green_candies
            red_candies -= blue_candies - green_candies
            blue_candies = green_candies

        if red_candies < green_candies:
            num_days += green_candies - red_candies
            blue_candies -= green_candies - red_candies
            green_candies = red_candies

        if red_candies >= 1:
            if (red_candies + blue_candies + green_candies) % 2 == 0:
                num_days += (red_candies + blue_candies + green_candies) // 2
            else:
                num_days += ((red_candies + blue_candies + green_candies) - 1) // 2

        max_days = max(max_days, num_days)
    print(max_days)


    ##### old: first attempt
    # max_days = 0
    # if green_candies == blue_candies:
    #     num_days = 0
    #     for idx_i, candy in enumerate(candies):
    #         # print(candies)
    #         # print("idx i")
    #         # print(idx_i)
    #         if idx_i < len(candies) - 1:
    #             while candies[idx_i] > 0:
    #                 for idx_j in range(len(candies) - 1, idx_i, - 1):
    #                     # print("idx_j")
    #                     # print(idx_j)
    #                     if candies[idx_j] > 0:
    #                         candies[idx_i] -= 1
    #                         candies[idx_j] -= 1
    #                         num_days += 1
    #                         if candies[idx_i] == 0:
    #                             # print("##")
    #                             break
    #             if candies[len(candies) - 1] == 0:
    #                 break
    #     max_days = max(num_days, max_days)
    # else:
    #     num_days = 0
    #     for idx_i, candy in enumerate(candies):
    #         # print(candies)
    #         # print("idx i")
    #         # print(idx_i)
    #         if idx_i < len(candies) - 1:
    #             idx_j = len(candies) - 1
    #             while candies[idx_i] > 0 and idx_i < idx_j:
    #                 while candies[idx_j] > 0 and idx_i < idx_j:
    #                     candies[idx_i] -= 1
    #                     candies[idx_j] -= 1
    #                     num_days += 1
    #                     if candies[idx_i] == 0:
    #                         break
    #                 idx_j -= 1
    #                 # for idx_j in range(len(candies) - 1, idx_i, - 1):
    #                 #     # print("idx_j")
    #                 #     # print(idx_j)
    #                 #     if candies[idx_j] > 0:
    #                 #         candies[idx_i] -= 1
    #                 #         candies[idx_j] -= 1
    #                 #         num_days += 1
    #                 #         if candies[idx_i] == 0:
    #                 #             # print("##")
    #                 #             break
    #             if candies[len(candies) - 1] == 0:
    #                 break
    #     max_days = max(num_days, max_days)
    # print(candies)

    #### old: second attempt
    # num_days = 0
    # num_days += red_candies
    # blue_candies -= red_candies
    # red_candies -= red_candies

    # if blue_candies > 0:
    #     if blue_candies >= green_candies:
    #         num_days += green_candies
    #         blue_candies -= green_candies
    #         green_candies -= green_candies
    #     else:
    #         num_days += blue_candies
    #         green_candies -= blue_candies
    #         blue_candies -= blue_candies

    # max_days = max(max_days, num_days)

    # red_candies, green_candies, blue_candies = candies[0], candies[1], candies[2]

    # num_days = 0
    # num_days += red_candies
    # if red_candies % 2 == 0:
    #     blue_candies -= red_candies // 2
    #     green_candies -= red_candies // 2
    # else:
    #     blue_candies -= ((red_candies - 1) // 2) + 1
    #     green_candies -= (red_candies - 1) // 2

    # if blue_candies > 0:
    #     if blue_candies >= green_candies:
    #         num_days += green_candies
    #         blue_candies -= green_candies
    #         green_candies -= green_candies
    #     else:
    #         num_days += blue_candies
    #         green_candies -= blue_candies
    #         blue_candies -= blue_candies

    # max_days = max(max_days, num_days)
    # print(max_days)