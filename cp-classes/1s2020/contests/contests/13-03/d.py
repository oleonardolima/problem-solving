n_students = int(input())
skills = list(input().split(" "))
skills = [int(skill) for skill in skills]

skills = sorted(skills)

n_problems = 0

ptr1 = n_students - 1
ptr2 = n_students - 2
while ptr2 >= 0:
    if (skills[ptr1] == skills[ptr2]):
        ptr1 -= 2
        ptr2 -= 2
    else:
        n_problems += 1
        skills[ptr2] += 1

print(n_problems)