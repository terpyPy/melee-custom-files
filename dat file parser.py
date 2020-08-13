import re
import pprint

CFFormat = ['CF ##']
zeroSevenFormat = ['070707']
fourTwoFourEightFormat = ['4248']
formatsArr = [CFFormat, fourTwoFourEightFormat, zeroSevenFormat]
formats = ['CF 00', 'CF 08', 'CF 07', 'CF 0F', 'CF F0', 'CF 09', 'CF 04',
           '42 48',
           '07 07 07']
hexLine = ''
twoHexLines = ''
matchDict = {}
offsetRE = re.compile(r'.*([\da-fA-F]{8})'
                      r'.*([\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} '
                      r'[\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} '
                      r'[\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2})')
def match_check(format, line, formatType):
    if (format in line) and (offset not in matchDict):
        matchDict[offset] = line
        formatType.append(offset)
def cycle(line):
    x = 0
    for i in range(len(formats)):
        match_check(formats[i], line, formatsArr[x])
        if i >= 6:
            x += 1


with open(input('please give a file name ')) as TXT_file:
    for line in TXT_file:
        hexMatch = offsetRE.search(line)
        if hexMatch is not None:
            offset, hexLine = hexMatch.groups()
        cycle(hexLine)
        twoHexLines = hexLine + ' ' + twoHexLines
        if len(twoHexLines) > 100:
            twoHexLines = ''
        cycle(twoHexLines)
pprint.pprint(matchDict)
pprint.pprint(zeroSevenFormat)
pprint.pprint(fourTwoFourEightFormat)
pprint.pprint(CFFormat)
TXT_file.close()
