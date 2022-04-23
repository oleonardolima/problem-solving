n = int(input())
arr = list(input().split(" "))
arr = [int(arr_element) for arr_element in arr]

arr.sort()
if n == 2:
    print(0)
else:
    first_min = arr[0]
    second_min = first_min

    first_max = first_min
    second_max = first_max

    initial_instability = max(arr) - min(arr[1:])

    for num in arr:
        if num <= first_min:
            first_min = num
        elif num >= first_max:
            second_max = first_max
            first_max = num

    if second_max - first_min < initial_instability:
        initial_instability = second_max - first_min

    print(initial_instability)
