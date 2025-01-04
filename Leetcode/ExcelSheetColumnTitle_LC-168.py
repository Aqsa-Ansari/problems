import math

columnNumber = 2147483647

def convertToTitle(columnNumber):
    output = ""
    while(columnNumber > 26):
        qoutient = math.floor(columnNumber / 26)
        remainder = columnNumber % 26
        if remainder == 0:
            remainder = 26
            qoutient = qoutient - 1
        if qoutient > 26:
            output = convertToTitle(qoutient)
        else:
            output = chr(qoutient + 64)
        columnNumber = remainder
    return output + chr(columnNumber + 64)

print(convertToTitle(columnNumber))