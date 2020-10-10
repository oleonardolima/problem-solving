def unique_digits(number):
    visited_numbers = [0 for i in range(10)]
    digits = list(str(number))
    #print(digits)
    for num in digits:
        num = int(num)
        if visited_numbers[num] == 1:
            return False
        else:
            visited_numbers[num] += 1
    return True

year_number = int(input())

while True:
    year_number += 1
    if unique_digits(year_number):
        break

print(year_number)