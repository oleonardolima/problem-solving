beginning_number = int(input())
winner = ""
turn = "mahmoud"
while True:
    if turn == "mahmoud":
        a_number = 0
        if beginning_number % 2 == 0:
            a_number = beginning_number
            beginning_number -= a_number
        if beginning_number == 0:
            winner = "Mahmoud"
            break
        beginning_number -= 1
        turn = "ehab"
    else:
        a_number = 0
        if beginning_number % 2 != 0:
            a_number = beginning_number
            beginning_number -= a_number
        if beginning_number == 0:
            winner = "Ehab"
            break
        beginning_number -= 1
        turn = "ehab"
print(winner)
