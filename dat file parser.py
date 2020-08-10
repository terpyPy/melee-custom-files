import re
import pprint

CFFormat = ['CF ##']
zeroSevenFormat = ['070707']
fourTwoFourEightFormat = ['4248']
hexLine = ''
twoHexLines = ''
matchDict = {}
offsetRE = re.compile(r'.*([\da-fA-F]{8})'
                      r'.*([\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} '
                      r'[\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} '
                      r'[\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2})')


with open(input('please give a file name')) as TXT_file:
    for line in TXT_file:
        hexMatch = offsetRE.search(line)
        if hexMatch is not None:
            offset, hexLine = hexMatch.groups()

        if '07 07 07' in hexLine:
            matchDict[offset] = hexLine
            zeroSevenFormat.append(offset)

        if 'CF 00' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)

        if 'CF 04' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)

        if 'CF 08' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)

        if '42 48' in hexLine:
            matchDict[offset] = hexLine
            fourTwoFourEightFormat.append(offset)
        if 'CF 07' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)
        if 'CF 0F' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)
        if 'CF F0' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)
        if 'CF 09' in hexLine:
            matchDict[offset] = hexLine
            CFFormat.append(offset)

        twoHexLines = hexLine + ' ' + twoHexLines

        if len(twoHexLines) > 100:
            twoHexLines = ''

        if '07 07 07' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in zeroSevenFormat:
                zeroSevenFormat.append(offset)

        if 'CF 00' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

        if '42 48' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in fourTwoFourEightFormat:
                fourTwoFourEightFormat.append(offset)

        if 'CF 07' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

        if 'CF 0F' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

        if 'CF F0' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

        if 'CF 09' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

        if 'CF 08' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

        if 'CF 04' in twoHexLines:
            matchDict[offset] = twoHexLines
            if offset not in CFFormat:
                CFFormat.append(offset)

pprint.pprint(matchDict)
pprint.pprint(zeroSevenFormat)
pprint.pprint(fourTwoFourEightFormat)
pprint.pprint(CFFormat)
TXT_file.close()
