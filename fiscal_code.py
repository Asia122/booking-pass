import pandas as pd

"""
The fiscal_code module has multiple functions
with the purpose of calculating the Italian fiscal code
given name, surname, date of birth, gender, and place of birth.
The input in the functions is not checked because
it is checked in the part that calls the fiscal_code_calculator funciton.
"""


def fiscal_code_calculator(name, surname, dob, gender, pob):
    """
    This function comes into play when the adder,
    after having asked all the personal information,
    have to calculate the fiscal code.
    The function recalls all the other functions
    that build piece by piece the Italian fiscal code.
    """

    initial_fiscal_code = get_surname_letters(surname)
    initial_fiscal_code = initial_fiscal_code + get_name_letters(name)
    initial_fiscal_code = initial_fiscal_code + get_birth_data(dob, gender)
    initial_fiscal_code = initial_fiscal_code + get_place_data(pob)
    fiscal_code = initial_fiscal_code + get_control_char(initial_fiscal_code)

    return fiscal_code


def get_surname_letters(surname):
    """
    This funciton returns the first 3 letters
    of the Italian fiscal code as string.
    These part is represented by the
    first 3 consonants of the surname are used.
    If the surname has less than 3 consonants,
    the vowels will replace the blank spaces.
    If the whole surname has less than 3 letters,
    the blank spaces are replaced with an X.
    """

    surname = surname.upper()
    result = ""
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    to_analyze = 0
    still_consonants = True
    still_vowels = True

    while len(result) < 3:
        if still_consonants:
            if surname[to_analyze] in consonants:
                result += surname[to_analyze]
        elif still_vowels:
            if surname[to_analyze] in vowels:
                result += surname[to_analyze]
        else:
            result += "X"

        if to_analyze + 1 != len(surname):
            to_analyze += 1
        elif to_analyze + 1 == len(surname) and still_consonants:
            to_analyze = 0
            still_consonants = False
        else:
            still_vowels = False

    return result


def get_name_letters(name):
    """
    This funciton returns the second 3 letters
    of the Italian fiscal code as string.
    The first three consonants of the name are used.
    If the name has less than 3 consonants,
    then vowels will replace the blank spaces.
    If the whole name has less than 3 letters,
    the blank spaces are filled with an X.
    If the name has more than 3 consonants,
    the 2nd is skipped.
    """

    name = name.upper()
    result = ""
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    to_analyze = 0
    still_consonants = True
    still_vowels = True

    while len(result) < 4:
        if still_consonants:
            if name[to_analyze] in consonants:
                result += name[to_analyze]
        elif still_vowels:
            if name[to_analyze] in vowels:
                result += name[to_analyze]
        else:
            result += "X"

        if to_analyze + 1 != len(name):
            to_analyze += 1
        elif to_analyze + 1 == len(name) and still_consonants:
            to_analyze = 0
            still_consonants = False
        else:
            still_vowels = False

    if consonants_counter(name) > 3:
        result = result[0] + result[2:4]
    else:
        result = result[:3]

    return result


def consonants_counter(word):
    """
    This function returns the number
    of consonants in a word.
    In the program is used by the function
    that returns the letters to insert in
    the Italian fiscal code due to the
    second-consonant skipping rule.
    """

    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    result = 0

    for letter in word.upper():
        if letter in consonants:
            result += 1

    return result


def get_birth_data(dob, gender):
    """
    This function returns an alphanumeric string
    that represents the part of the Italian fiscal
    code derivated by the date of birth of the person.
    The string is composed by:
    - Year of birth (2 digits): the last 2 year of birth digits are used;
    - Month of birth (1 letter): each single month is associated with 1 letter;
    - Birthday (2 digits): 2 birthday digits used, if is a woman 40 is added.
    """

    year = dob[-2:]
    month_letter = ["A", "B", "C", "D", "E", "H", "L", "M", "P", "R", "S", "T"]
    month = int(dob[3:5])
    day = int(dob[:2])

    if gender == "F":
        day += 40

    return year + month_letter[month - 1] + str(day)


def get_place_data(pob):
    """
    This function returns the Belfiore code
    used in the cadastral code which comprises
    one letter, then three digits.
    Each municipality has its code and
    people born in a foreign country
    have their own code according to the country of birth.
    """

    pob = pob.lower()
    belfiore = pd.read_csv("registry_codes.csv")

    return belfiore["Code"].loc[belfiore["Place"] == pob].to_string()[-4:].upper()


def get_control_char(initial_fiscal_code):
    """
    This function, given the first 15
    characters of the fiscal code, is able
    to return the control character.
    This letter is determined as follows:
    - the 8 odd characters are set apart; same thing for the 7 even ones;
    - each single character converted into a numeric value;
    - all the values are to be added, the final result has to be divided by 26;
    - the remainder will give the last character.
    """

    even_dict = {"0": 0,
                 "1": 1,
                 "2": 2,
                 "3": 3,
                 "4": 4,
                 "5": 5,
                 "6": 6,
                 "7": 7,
                 "8": 8,
                 "9": 9,
                 "A": 0,
                 "B": 1,
                 "C": 2,
                 "D": 3,
                 "E": 4,
                 "F": 5,
                 "G": 6,
                 "H": 7,
                 "I": 8,
                 "J": 9,
                 "K": 10,
                 "L": 11,
                 "M": 12,
                 "N": 13,
                 "O": 14,
                 "P": 15,
                 "Q": 16,
                 "R": 17,
                 "S": 18,
                 "T": 19,
                 "U": 20,
                 "V": 21,
                 "W": 22,
                 "X": 23,
                 "Y": 24,
                 "Z": 25}
    even_chars = []
    odd_dict = {"0": 1,
                "1": 0,
                "2": 5,
                "3": 7,
                "4": 9,
                "5": 13,
                "6": 15,
                "7": 17,
                "8": 19,
                "9": 21,
                "A": 1,
                "B": 0,
                "C": 5,
                "D": 7,
                "E": 9,
                "F": 13,
                "G": 15,
                "H": 17,
                "I": 19,
                "J": 21,
                "K": 2,
                "L": 4,
                "M": 18,
                "N": 20,
                "O": 1,
                "P": 3,
                "Q": 6,
                "R": 8,
                "S": 12,
                "T": 14,
                "U": 16,
                "V": 10,
                "W": 22,
                "X": 25,
                "Y": 24,
                "Z": 23}
    odd_chars = []
    sum_chars = 0
    remainder_dict = {0: "A",
                      1: "B",
                      2: "C",
                      3: "D",
                      4: "E",
                      5: "F",
                      6: "G",
                      7: "H",
                      8: "I",
                      9: "J",
                      10: "K",
                      11: "L",
                      12: "M",
                      13: "N",
                      14: "O",
                      15: "P",
                      16: "Q",
                      17: "R",
                      18: "S",
                      19: "T",
                      20: "U",
                      21: "V",
                      22: "W",
                      23: "X",
                      24: "Y",
                      25: "Z"}

    for position in enumerate(initial_fiscal_code):
        if (position[0] + 1) % 2 == 0:
            even_chars += [initial_fiscal_code[position[0]]]
        else:
            odd_chars += [initial_fiscal_code[position[0]]]

    for even_char in even_chars:
        sum_chars += even_dict[even_char]

    for odd_char in odd_chars:
        sum_chars += odd_dict[odd_char]

    remainder = sum_chars % 26

    return remainder_dict[remainder]
