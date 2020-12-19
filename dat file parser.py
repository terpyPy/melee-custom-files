import re
import pprint
import PySimpleGUI as sg
import os

CFFormat = ['CF ##']
zeroSevenFormat = ['070707']
fourTwoFourEightFormat = ['4248']
nineEightZeroZeroFormat = ['9800 ##']
formatsArr = [CFFormat, fourTwoFourEightFormat, zeroSevenFormat, nineEightZeroZeroFormat]
formats = ['CF 00', 'CF 08', 'CF 07', 'CF 0F', 'CF F0', 'CF 09', 'CF 04', 'CF 0C',
           '42 48',
           '07 07 07',
           '07 07 07 04',
           '98 00']
luigi = {'0000F3B0': 'aura around fireball', '0000F430': ' Aura around fireball',
         '0000F4D0': 'Affects the color of the fireball slightly',
         '000111E0': 'Inside of ring created when using neutral B',
         '00011A70': 'Outer part of tornado',
         '00011B40': 'Upper part of tornado',
         '00011C10': 'One side of inner tornado',
         '00011DA0': 'Underneath tornado effect',
         '000000E0': 'Smoke around hand for fireball',
         '000000F0': 'More smoke around hand',
         '00000190': 'Smoke behind fireball',
         '000001A0': 'Smoke behind fireball',
         '000001B0': 'Faint smoke behind fireball',
         '00000260': 'Ball particles upon fireball hitting a wall',
         '00000270': 'More ball particles',
         '000002D0': 'More ball particles',
         '000002E0': 'Particles around fireball',
         '00000360': 'More dust',
         '000003F0': 'Square particles behind fireball',
         '00011260': 'Starting color of ring around hand after using fireball',
         '00011AF0': 'Outer ring of tornado as it finishes',
         '00011BC0': 'Another finishing part of tornado',
         '00011C90': 'One side of finishing tornado effect',
         '00011E20': 'Tornado effect below Luigi',
         '00011D60': 'Other side of finishing tornado effect',
         '00000350': 'Dust from fireball collision',
         '00011CE0': 'Other side of inner tornado'}
captain_falcon = {'00000120':'Trailing Smoke Down B 1',
                  '00000140':'Trailing Smoke Down B 2',
                  '00000150':'Trailing Smoke Down B 3',
                  '00000160':'Trailing Smoke Down B 4',
                  '00000170':'Trailing Smoke Down B 5',
                  '000001D0':'Trailing Smoke Neutral B 1',
                  '000001E0':'Trailing Smoke Neutral B 2',  # not found cf 05 not in list
                  '00000210':'Trailing Smoke Neutral B 3',
                  '00000290':'Square Dots Neutral B 1',
                  '000002A0':'Square Dots Neutral B 2',
                  '000003A0':'Smoke on wings of Neutral B 1',
                  '000003B0':'Smoke on wings of Neutral B 2',
                  '000003E0':'Smoke on wings of Neutral B 3',
                  '00000470':'Square Dots Down B 1',
                  '00000480':'Square Dots Down B 2',
                  '000004D0':'Circle Dots Down B 1',
                  '000004E6':'Circle Dots Down B 2',  # not found unknown cf format
                  '00000530':'Circle Dots Down B 3',
                  '00000580':'Trailing Smoke Down B 1',
                  '000005A0':'Trailing Smoke Down B 2',
                  '000005B0':'Trailing Smoke Down B 3',
                  '000005C0':'Trailing Smoke Down B 4',
                  '000005D0':'Trailing Smoke Down B 5',
                  '00000630':'Trailing Smoke Down B and After Smoke of Over B 1',
                  '00000640':'Trailing Smoke Down B and After Smoke of Over B 2',
                  '00000650':'Trailing Smoke Down B and After Smoke of Over B 3',
                  '000006A0': 'Front of Down B',
                  '00000760': 'Smoke of Over B large',
                  '00000770': 'Smoke of Over B small',
                  '00000780': 'Smoke Behind Falcon Over B 1',
                  '00000790': 'Smoke Behind Falcon Over B 2',
                  '00000820': 'Square Dots Over B 1',
                  '00000830': 'Square Dots Over B 2',
                  '000008A0': 'Smoke after Over B 1',
                  '000008B0': 'Smoke after Over B 2',
                  '00000910': 'Smoke after neutral B 1',
                  '00000920': 'Smoke after neutral B 2',
                  '00000950': 'Smoke after neutral B 3',
                  '0001DE00': 'Tip of the falcon kick',
                  '000202E0': 'Tip of the falcon punch',
                  '00022D60': 'Part of Falcon punch lens flare extending lines Beginning 1',
                  '00022E30': 'Part of Falcon punch lens flare extending lines Beginning 2',
                  '00022EF0': 'Part of Falcon punch lens flare extending lines Beginning 3',
                  '00022FC0': 'Part of Falcon punch lens flare extending lines Beginning 4',
                  '00023090': 'Part of Falcon punch lens flare extending lines Beginning 5',
                  '00023160': 'Part of Falcon punch lens flare extending lines Beginning 6',
                  '00023220': 'Part of Falcon punch lens flare extending lines Beginning 7',
                  '000232F0': 'Part of Falcon punch lens flare extending lines Beginning 8',
                  '000233C0': 'Part of Falcon punch lens flare extending lines Beginning 9',
                  '00023490': 'Part of Falcon punch lens flare extending lines Beginning 10',
                  '00024B70': 'Raptor Boost Hand Lens Flare Beginning',
                  '00022D10': 'Falcon Punch Small Lens Flare Beginning',
                  '000235D0': 'Falcon Punch Big Lens Flare Beginning',
                  '00025440': 'Part of the Raptor Boost Smoke'}
falco_fox = {'0001AC80': 'Tip of the Firefox',
             '0001C2A0': 'Shine',
             '0001C8E0': 'First Frames of Shine: Inner Hexagon',
             '0001C950': 'First Frames of Shine: Outer Hexagon Glow 1',
             '0001CA90': 'First Frames of Shine: Outer Hexagon Glow 2',
             '2': '',
             '3': '',
             '4': '',
             }

hexLine = ''
twoHexLines = ''
matchDict = {}
offsetRE = re.compile(r'.*([\da-fA-F]{8})'
                      r'.*([\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} [\da-fA-F]{2} '
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
        if i == 7:
            x += 1
        if i == 8:
            x += 1
        if i == 9:
            x += 0
        if i == 10:
            x += 1


sg.theme('DarkBlack')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.T('Chose file to parse')], [sg.In(), sg.FileBrowse(), sg.Button('Cancel')],
          [sg.Output(size=(88, 20), key='output')], [sg.Button('parse file', bind_return_key=True),
           sg.Button('Clear parsed data'), sg.Button('Write to txt file'),
           sg.Button('Luigi data'), sg.Button('Falcon data'), sg.Button('Spacies data')]]

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
                if hexMatch:
                    offset, hexLine = hexMatch.groups()
                cycle(hexLine)
                twoHexLines = hexLine[0:20]
                cycle(twoHexLines)
                twoHexLines = ''

            pprint.pprint(matchDict)
            pprint.pprint(formatsArr)
            TXT_file.close()
            sg.popup('parse complete', any_key_closes=True)

    if event == 'Clear parsed data':
        CFFormat *= 0
        zeroSevenFormat *= 0
        fourTwoFourEightFormat *= 0
        nineEightZeroZeroFormat *= 0
        CFFormat.append('CF ##')
        zeroSevenFormat.append('070707')
        fourTwoFourEightFormat.append('4248')
        nineEightZeroZeroFormat.append('9800 ##')
        hexLine = ''
        twoHexLines = ''
        matchDict = {}

    if event == 'Write to txt file':
        path = os.path.dirname(os.path.abspath(__file__))
        with open('dat_file_output.txt', 'w') as fp:
            for key, val in matchDict.items():
                fp.write('%s:%s\n' % (key, val))

            for listItem in formatsArr:
                fp.write('%s\n' % listItem)
        fp.close()
        window['output'].update('saved to dat_file_otput.txt')

    if event == 'Luigi data':
        for i in matchDict:
            if i in luigi:
                pprint.pprint(i + ' - ' + luigi[i])
        for i in luigi:
            if i not in matchDict:
                pprint.pprint('not found: ' + i + ' - ' + luigi[i])

    if event == 'Falcon data':
        for i in matchDict:
            if i in captain_falcon:
                pprint.pprint(i + ' - ' + captain_falcon[i])

    if event == 'Spacies data':
        for i in matchDict:
            if i in falco_fox:
                pprint.pprint(i + ' - ' + falco_fox[i])
