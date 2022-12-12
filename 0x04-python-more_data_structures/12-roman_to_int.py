def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 1001
        for c in roman_string:
            if rom_dict[c] > prev:
                total += rom_dict[c] - (prev * 2)
            else:
                total += rom_dict[c]
            prev = rom_dict[c]
        return total
    return 0
