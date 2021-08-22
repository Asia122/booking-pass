"Function that given name, surname, date of birth, gender, and place of birth is able to calculate the Italian fiscal code."

def FiscalCodeCalculator(name, surname, dob, gender, pob):
    fiscalCode = GetSurnameLetters(surname) + GetNameLetters(name) + GetBirthData(dob, gender) + GetPlaceData(pob)

    return fiscalCode + GetControlChar(fiscalCode)

def GetSurnameLetters(surname):
    surname = surname.upper()
    result = ""
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    toAnalyze = 0
    stillConsonants = True
    stillVowels = True

    while len(result) < 3:
        if stillConsonants:
            if surname[toAnalyze] in consonants:
                result += surname[toAnalyze]
        elif stillVowels:
            if surname[toAnalyze] in vowels:
                result += surname[toAnalyze]
        else:
            result += "X"

        if toAnalyze + 1 != len(surname):
            toAnalyze += 1
        elif toAnalyze + 1 == len(surname) and stillConsonants:
            toAnalyze = 0
            stillConsonants = False
        else:
            stillVowels = False
        
    return result