num_exams = int(input())
exams = []
for exam in range(num_exams):
    input_ = [int(day) for day in input().split(" ")]
    exams.append(tuple(input_))

exams.sort(key=lambda x:x[0])
# print(exams)

curr_day = -1
for exam in exams:
    #print(curr_day)
    if exam[1] < curr_day:
        curr_day = int(exam[0])
    else:
        curr_day = int(exam[1])

print(curr_day)