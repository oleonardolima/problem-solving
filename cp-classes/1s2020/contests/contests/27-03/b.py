input_ = list(input().split(" "))
number_buckets = int(input_[0])
garden_length = int(input_[-1])

buckets = [int(bucket) for bucket in input().split(" ")]

buckets = sorted(buckets)
possible_bucket = 0
for bucket in buckets:
    if bucket > garden_length:
        break

    if garden_length % bucket == 0:
        possible_bucket = bucket
    
# print(possible_bucket)
num_hours = garden_length // possible_bucket

print(num_hours)