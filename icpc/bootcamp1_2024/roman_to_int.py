"""
given a roman number convert it into decimal
for ex :
    X -> 10
    IV -> 4
"""


roman_to_decimal = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

roman = input()
roman = roman.replace("IV","IIII")
roman = roman.replace("IX","VIIII")
roman = roman.replace("XL","XXXX")
roman = roman.replace("XC","LXXXX")
roman = roman.replace("CD","CCCC");
roman = roman.replace("CM","DCCCC");

result = 0
for r in roman:
    result += roman_to_decimal[r]

print(result)
