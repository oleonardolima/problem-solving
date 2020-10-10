input_ = list(input().split(" "))

students_number = int(input_[0])
team_size = int(input_[-1])

students_rating = list(input().split(" "))

lookup = {}
for idx, student in enumerate(students_rating):
    if len(lookup) >= team_size:
        break
    if student not in lookup:
        lookup[student]  = idx + 1

if len(lookup) < team_size:
    print("NO")
else:
    team = []
    for student in lookup:
        team.append(str(lookup[student]))
        team.append(" ")
    print("YES")
    print("".join(team[:-1]))