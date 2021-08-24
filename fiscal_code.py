"Function that given name, surname, date of birth, gender, and place of birth is able to calculate the Italian fiscal code."

def FiscalCodeCalculator(name, surname, dob, gender, pob):
    initialFiscalCode = GetSurnameLetters(surname) + GetNameLetters(name) + GetBirthData(dob, gender) + GetPlaceData(pob)

    return initialFiscalCode + GetControlChar(initialFiscalCode)

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


def GetNameLetters(name):
    name = name.upper()
    result = ""
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    toAnalyze = 0
    stillConsonants = True
    stillVowels = True

    while len(result) < 4:
        if stillConsonants:
            if name[toAnalyze] in consonants:
                result += name[toAnalyze]
        elif stillVowels:
            if name[toAnalyze] in vowels:
                    result += name[toAnalyze]
        else:
                result += "X"

        if toAnalyze + 1 != len(name):
            toAnalyze += 1
        elif toAnalyze + 1 == len(name) and stillConsonants:
            toAnalyze = 0
            stillConsonants = False
        else:
            stillVowels = False

    if ConsonantsCounter(name) > 3:
        result = result[0] + result[2:4]   
    else:
        result = result[:3]
      
    return result


def ConsonantsCounter(word):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    result = 0

    for x in word.upper():
        if x in consonants:
            result += 1
    
    return result


def GetBirthData(dob, gender):
    year = dob[-2:]
    monthLetter = ["A", "B", "C", "D", "E", "H", "L", "M", "P", "R", "S", "T"]
    month = int(dob[3:5])
    day = int(dob[:2])

    if gender == "F":
        day += 40

    return year + monthLetter[month - 1] + str(day)


def GetPlaceData(pob): 
    import pandas as pd 

    pob = pob.lower() 
    codes = pd.read_csv("registry_codes.csv")
    
    return codes.loc[codes["Place"] == pob]["Code"].to_string()[-4:].upper()


def GetControlChar(initialFiscalCode):
    evenDict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
    evenChars = []
    oddDict = {"0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21, "A": 1, "B": 0, "C": 5, "D": 7, "E": 9, "F": 13, "G": 15, "H": 17, "I": 19, "J": 21, "K": 2, "L": 4, "M": 18, "N": 20, "O": 1, "P": 3, "Q": 6, "R": 8, "S": 12, "T": 14, "U": 16, "V": 10, "W": 22, "X": 25, "Y": 24, "Z": 23}
    oddChars = []
    sumChars = 0
    remainderDict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

    for position in range(len(initialFiscalCode)):
        if (position + 1) % 2 == 0:
            evenChars += [initialFiscalCode[position]]
        else:
            oddChars += [initialFiscalCode[position]]

    for evenChar in evenChars:
        sumChars += evenDict[evenChar]

    for oddChar in oddChars:
        sumChars += oddDict[oddChar]

    remainder = sumChars % 26
    
    return remainderDict[remainder]



print(FiscalCodeCalculator("Asia", "Martini", "12/02/1999", "F", "Conegliano") == "MRTSAI99B52C957F", FiscalCodeCalculator("Asia", "Martini", "12/02/1999", "F", "Conegliano"))