from collections import defaultdict
num_queries = int(input())
for _ in range(num_queries):
    num_cards = int(input())
    pin_codes = []
    for _ in range(num_cards):
        #pin = int(input())
        #pin = [int(digit) for digits in input()]
        pin = input()
        pin_codes.append(pin)
    #print(pin_codes)

    min_digits_changed = 0
    used_pin_codes = defaultdict(int)
    modified_pin_codes = []
    used_modified_pin_codes = {}
    for pin in pin_codes:
        if pin not in used_pin_codes:
            used_pin_codes[pin] += 1
            modified_pin_codes.append(pin)
            used_modified_pin_codes[pin] = True
            continue

        used_pin_codes[pin] += 1
        min_digits_changed += 1

        is_break = False
        pin = [digit for digit in pin]
        for idx, digit in enumerate(pin):
            pin = [digit for digit in pin]
            for new_digit in range(10):
                pin[idx] = str(new_digit)
                str_pin = "".join(pin)
                if  str_pin not in used_modified_pin_codes:
                    modified_pin_codes.append(str_pin)
                    used_modified_pin_codes[str_pin] = True
                    is_break = True
                    break
            pin = [digit for digit in pin]
            if is_break:
                break

        # possible_digits = [digit for digits in range(10)]
        # pos_change = 0
        # new_digits = [0, 0, 0, 0]
        # for idx, digit in enumerate(pin):
        #     old_digit = digit
        #     for possible_digit in possible_digits:
        #         pin[idx] = possible_digit
        #         if pin not in used_pin_codes:
        #             used_pin_codes[pin]
        #             new_digits[idx] = possible_digit
        #             break
        #     for n in new_digits:
        #         if n != 0:
        #             min_digits_changed += 1

    #print(modified_pin_codes)
    print(min_digits_changed)
    for pin in modified_pin_codes:
        print(pin)
