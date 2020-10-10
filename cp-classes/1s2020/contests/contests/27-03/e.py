# Functions
def get_ocurrences(elements):
    ocurrences = {}
    for idx, element in enumerate(elements):
        if element not in ocurrences:
            #print(idx)
            ocurrences[element] = [1, [idx]]
        else:
            ocurrences[element][0] += 1
            ocurrences[element][1].append(idx)
    return ocurrences

def has_equal_elements(ocurrences):
    for key in ocurrences:
        if ocurrences[key][0] >= 2:
            return True
    return False

# End of Functions

number_elements = int(input())
elements = [int(element) for element in input().split(" ")]

ocurrences = get_ocurrences(elements)
#print(ocurrences)

while(has_equal_elements(ocurrences)):
    #print(ocurrences)
    for element in elements:
        print(ocurrences)
        # print(elements)
        #print("count: {}".format(ocurrences[element][0]))
        if ocurrences[element][0] >= 2:
            ocurrences[element][0] -= 2

            idx = ocurrences[element][1][0]
            del ocurrences[element][1][0]
            elements[idx] = -1

            idx = ocurrences[element][1][0]
            del ocurrences[element][1][0]
            elements[idx] = 2 * elements[idx]

            if elements[idx] not in ocurrences:
                ocurrences[elements[idx]] = [1, [idx]]
            else:
                # print(elements[idx])
                # print(ocurrences[elements[idx]])
                ocurrences[elements[idx]][0] += 1
                ocurrences[elements[idx]][1].append(idx)
                ocurrences[elements[idx]][1].sort()
            #ocurrences = get_ocurrences(elements)
    #print(elements)

# print(elements)
for element in elements[:]:
    if element < 0:
        #print("*")
        elements.remove(element)

print(len(elements))
print(" ".join(map(str, elements)))
