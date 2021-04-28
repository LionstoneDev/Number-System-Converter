class Error(Exception):
    pass
def biggest_number_factor(number, base):
    x = 0
    factor = x
    while base**x <= number:
        factor = x
        x += 1
    return factor
def convertFromDec(decimal:int, base:int):
    negative = False
    decimal=int(decimal)
    if base < 2 or base > 36:
        raise Error("Only base numbers from 2 to 36 are allowed.")
    if decimal < 0:
        negative=True
        decimal=decimal*-1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    numbArray = []
    endNum = ""
    baseNums = []
    charsFromAlphabet = 0
    for x in range(int(biggest_number_factor(decimal, base)+1)):
        x = "$"
        numbArray.append(x)
    factor = biggest_number_factor(decimal, base)
    for x in range(0, base):
        baseNums.append(x)
    baseNums = baseNums[::-1]
    for x in numbArray:
        for y in baseNums:
            if decimal-(y*base**factor) < 0:
                continue
            else:
                numbArray[counter] = y
                decimal -= y*base**factor
                counter += 1
                factor -= 1
                break
    charsFromAlphabet = base-10
    charsToUse = []
    for x in range(charsFromAlphabet):
        charsToUse.append(alphabet[x])
    charsToUse = charsToUse[::-1]
    for x in numbArray:
        if x > 9:
            numbArray[numbArray.index(x)] = charsToUse[(base-1) - x]
    for num in numbArray:
        endNum = f"{endNum}{str(num)}"
    if negative:
        endNum=f"-{endNum}"
    return endNum
def convertToDec(number:str, base:int):
    if base < 2 or base > 36:
        raise Error("Only base numbers from 2 to 36 are allowed.")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbArray = []
    for x in str(number):
        numbArray.append(x)
    factor = len(numbArray)-1
    decimal = 0
    for x in numbArray:
        if x in alphabet:
            numbArray[numbArray.index(x)] = 10+alphabet.index(x)
    for x in numbArray:
        decimal += int(x)*base**factor
        factor-=1
    return decimal
def convert(number:str, numberSys:int, sysToConv:int):
    if numberSys==10:
        return convertFromDec(number, sysToConv)
    if sysToConv==10:
        return convertToDec(str(number), numberSys)
    else:
        converted = 0
        converted = convertToDec(number, numberSys)
        return convertFromDec(converted, sysToConv)