from collections import defaultdict
jon_input = [letter for letter in input()]
doctor_input = [letter for letter in input()]

jon_freq = defaultdict(int)
doctor_freq = defaultdict(int)

for letter in jon_input:
    jon_freq[letter] += 1

for letter in doctor_input:
    doctor_freq[letter] += 1

go_to_doctor = False
if jon_freq['a'] >= doctor_freq['a']:
    go_to_doctor = True

if go_to_doctor:
    print("go")
else:
    print("no")