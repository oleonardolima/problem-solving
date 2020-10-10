t_queries = int(input())

for query in range(t_queries):
    _input = [int(num) for num in input().split(" ")]
    num_students = _input[0]
    highest_possible_score = _input[1]

    scores = [int(num) for num in input().split(" ")]

    prev_average_score = sum(scores) / num_students

    ptr1 = num_students - 1
    if ptr1 > 0:
        while sum(scores) / num_students == prev_average_score and scores[0] < highest_possible_score and ptr1 > 0:
            if scores[ptr1] == 0:
                ptr1 -= 1
            else:
                grade_to_add = highest_possible_score - scores[0]
                if scores[ptr1] >= grade_to_add:
                    scores[0] += grade_to_add
                    scores[ptr1] -= grade_to_add
                else:
                    scores[0] += scores[ptr1]
                    scores[ptr1] = 0

    print(scores[0])