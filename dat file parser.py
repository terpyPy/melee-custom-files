import re
import pprint
import PySimpleGUI as sg
CFFormat = ['CF ##']
zeroSevenFormat = ['070707']
fourTwoFourEightFormat = ['4248']
nineEightZeroZeroFormat = ['9800 ##']
formatsArr = [CFFormat, fourTwoFourEightFormat, zeroSevenFormat, nineEightZeroZeroFormat]
formats = ['CF 00', 'CF 08', 'CF 07', 'CF 0F', 'CF F0', 'CF 09', 'CF 04',
           '42 48',
           '07 07 07',
           '98 00']
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


sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.T('Chose file to parse')], [sg.In(), sg.FileBrowse()],
          [sg.Output(size=(88, 20), key='output')],
          [sg.Button('parse file'), sg.Button('clear'), sg.FileBrowse(button_text='browse', key='file'),sg.Button('Cancel')]]

# Create the Window
window = sg.Window('dat file parser', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        window.close()
        break
    if event == 'parse file' and values[0] is not None:
        with open(values[0]) as TXT_file:
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
            pprint.pprint(formatsArr)
            TXT_file.close()
    if event == 'clear':
        window['output'].update('')