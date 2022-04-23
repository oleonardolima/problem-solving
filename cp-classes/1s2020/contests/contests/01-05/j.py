start_time = [int(time) for time in input().split(":")]
end_time = [int(time) for time in input().split(":")]

h1, m1 = start_time[0], start_time[1]
h2, m2 = end_time[0], end_time[1]

h1_in_minutes = h1*60
h2_in_minutes = h2*60

half_time_in_minutes = (h2_in_minutes + m2) - (h1_in_minutes + m1)
half_time = (h1_in_minutes + m1) + half_time_in_minutes // 2

h3 = half_time // 60
m3 = half_time % 60

print("{:02d}:{:02d}".format(h3, m3))