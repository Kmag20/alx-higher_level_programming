#!/usr/bin/python3

def roman_to_int(roman_string):
    """ Converts a Roman Numeral to an integer """
    thousands = {'MMM': 3000, 'MM': 2000, 'M': 1000}
    hundreds = {'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600, 'D': 500, 'CD': 400, 'CCC': 300, 'CC': 200, 'C': 100}
    tens = {'XC': 90, 'LXXX': 80 , 'LXX': 70 , 'LX': 60, 'L': 50, 'XL': 40, 'XXX': 30, 'XX': 20, 'X': 10}
    units = {'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6, 'V': 5, 'IV': 4, 'III': 3, 'II': 2, 'I': 1}

    number = 0
    for roman, value in thousands.items():
        if roman in roman_string:
            number += value
            break
    for roman, value in hundreds.items():
        if roman in roman_string:
            if 'XC' in roman_string:
                number += 0
                continue
            if 'CD' in roman_string:
                number += hundreds['CD']
            else:
                number += value
            break
    for roman, value in tens.items():
        if roman in roman_string:
            if 'IX' in roman_string:
                number += 0
            if 'XL' in roman_string:
                number += tens['XL']
            else: 
                number += value
            break
    for roman, value in units.items():
        if roman in roman_string:
            if 'IV' in roman_string:
                number += units['IV']
            else:    
                number += value
            break

    return (number)
