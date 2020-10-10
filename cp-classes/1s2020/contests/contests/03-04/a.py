num_inputs = int(input())
registration = {}
for line in range(num_inputs):
    request = input()
    if request not in registration:
        registration[request] = 1
        print("OK")
    else:
        temp_str = list(request)
        temp_str.append(str(registration[request]))
        temp_str = "".join(temp_str)
        registration[request] += 1
        print(temp_str)