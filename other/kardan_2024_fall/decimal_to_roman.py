roman_numerals = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]



input = 3549 #MMMDXLIX
output = ""
for key,value in roman_numerals:
    while input >= value:
        input -= value
        output += key


print(output)
