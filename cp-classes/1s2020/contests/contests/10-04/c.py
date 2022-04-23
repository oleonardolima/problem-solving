while True:
    input_ = [int(el) for el in input().split(" ")]
    if int(input_[0]) == 0:
        break
    len_ages = len(input_)
    if  len_ages > 1:
        ages = input_
        ages.sort()
        for idx, age in enumerate(ages):
            if idx != len(ages) - 1:
                print(age, end=" ")
            else:
                print(age, end="\n")
        #print(ages)
    #print(input_)