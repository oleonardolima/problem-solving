import collections
initial_num_errors = int(input())

initial_errors = [int(num) for num in input().split(" ")]

prev_freq = collections.defaultdict(int)
compilation_errors_freq = collections.defaultdict(int)
corrected_errors = [0]*2

for error in initial_errors:
    prev_freq[error] += 1

compilation_errors = [int(num) for num in input().split(" ")]
for error in compilation_errors:
    compilation_errors_freq[error] += 1

for error in prev_freq:
    if prev_freq[error] > compilation_errors_freq[error]:
        corrected_errors[0] = error
    prev_freq[error] = compilation_errors_freq[error]
    compilation_errors_freq[error] = 0

compilation_errors = [int(num) for num in input().split(" ")]
for error in compilation_errors:
    compilation_errors_freq[error] += 1

for error in prev_freq:
    if prev_freq[error] > compilation_errors_freq[error]:
        corrected_errors[1] = error
    prev_freq[error] = compilation_errors_freq[error]

#print(compilation_errors_freq)
print(corrected_errors[0])
print(corrected_errors[1])
