
values = (
    (1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"),
    (40, "XL"), (50, "L"), (90, "XC"), (100, "C"),
    (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")
)


def rom_arab_value(num):
    for i in values:
        if i[1] == num:
            return i[0]
        if i[0] == num:
            return i[1]

def rom_to_arab(rom):
    wynik = 0

    prev = 0
    act = 0

    for i in range(len(rom)-1, -1, -1):
        print(rom[i])
        act = rom_arab_value(rom[i])

        if prev > act:
            wynik -= act
        else:
            wynik += act
        prev = act

    return wynik

def arab_to_rom(arab):
    wynik = ""
    for value, numeral in reversed(values):
        while arab >= value:
            wynik += numeral
            arab -= value
    return wynik

#do poprawy

print(rom_to_arab("MMMCMXCIX"))
print(arab_to_rom(3999))