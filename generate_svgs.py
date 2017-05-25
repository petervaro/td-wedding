OUTPUT = 'svg/invitation-front-{}.svg'

ROWS = """\
<tspan style="font-style:normal;font-variant:normal;font-weight:normal;font-str\
etch:normal;font-size:40px;line-height:100%;font-family:Rubik;-inkscape-font-sp\
ecification:Rubik;font-variant-ligatures:normal;font-variant-caps:normal;font-v\
ariant-numeric:normal;font-feature-settings:normal;text-align:end;writing-mode:\
lr-tb;text-anchor:end;fill:url(#linearGradient4610);fill-opacity:1;stroke-width\
:0.76689309px" y="103.52242" x="160.86951" sodipodi:role="line" id="tspan8361">\
{NAME}</tspan>""", """\
<tspan style="font-style:normal;font-variant:normal;font-weight:normal;font-str\
etch:normal;font-size:40px;line-height:100%;font-family:Rubik;-inkscape-font-sp\
ecification:Rubik;font-variant-ligatures:normal;font-variant-caps:normal;font-v\
ariant-numeric:normal;font-feature-settings:normal;text-align:end;writing-mode:\
lr-tb;text-anchor:end;fill:url(#linearGradient4610);fill-opacity:1;stroke-width\
:0.76689309px" y="143.52242" x="160.86951" sodipodi:role="line" id="tspan8387">\
{NAME}</tspan>""", """\
<tspan style="font-style:normal;font-variant:normal;font-weight:normal;font-str\
etch:normal;font-size:40px;line-height:100%;font-family:Rubik;-inkscape-font-sp\
ecification:Rubik;font-variant-ligatures:normal;font-variant-caps:normal;font-v\
ariant-numeric:normal;font-feature-settings:normal;text-align:end;writing-mode:\
lr-tb;text-anchor:end;fill:url(#linearGradient4610);fill-opacity:1;stroke-width\
:0.76689309px" y="183.52242" x="160.86951" sodipodi:role="line" id="tspan8389">\
{NAME}</tspan>""", """\
<tspan style="font-style:normal;font-variant:normal;font-weight:normal;font-str\
etch:normal;font-size:40px;line-height:100%;font-family:Rubik;-inkscape-font-sp\
ecification:Rubik;font-variant-ligatures:normal;font-variant-caps:normal;font-v\
ariant-numeric:normal;font-feature-settings:normal;text-align:end;writing-mode:\
lr-tb;text-anchor:end;fill:url(#linearGradient4610);fill-opacity:1;stroke-width\
:0.76689309px" y="223.52242" x="160.86951" sodipodi:role="line" id="tspan8391">\
{NAME}</tspan>"""

NAMES = ((b'peti',),
         (b'zsuzsi', b'gyuri'),
         (b'doni', b'\xc3\xa1gi', b'laci'),
         (b'n\xc3\xb3ra',b'kira', b'paddy'),
         (b'zs\xc3\xb3fi', b'lali', b'zsuzsi'),
         (b'd\xc3\xb3ri', b'\xc3\xa1goston'),
         (b'ingi', b'laci'),
         (b'erika', b'lili\xc3\xa1na', b'attila'),
         (b'adri', b'lack\xc3\xb3', b'bal\xc3\xa1zs', b'zsombor'),
         (b'd\xc3\xb3ri nagyi',),
         (b'kl\xc3\xa1ri nagyi',),
         (b'ibi',),
         (b'd\xc3\xb3ri', b'zoli', b'blanka', b'emma'))

REPLACE = {b'\xc3\xa1': 'a',
           b'\xc3\xb3': 'o'}

def asciify(bytes):
    return ''.join(
        REPLACE.get(c.encode('utf-8'), c) for c in bytes.decode('utf-8'))

with open('invitation-front-prototype.svg') as src:
    src = src.read()
    for names in NAMES:
        tspans = []
        for row, name, mark in zip(ROWS, names, ','*(len(names) - 1) + '!'):
            tspans.append(row.format(NAME=name.decode('utf-8').upper() + mark))
        output = OUTPUT.format('-'.join(map(asciify, names))).replace(' ', '-')
        print('Writing to file:', output)
        with open(output, 'w') as dst:
            dst.write(src.format(NAMES=''.join(tspans)))

OUTPUT = 'svg/invitation-back-{}.svg'

DATES = {'wedding' : '2017. július 27.',
         'party'   : '2017. augusztus 20.'}

with open('invitation-back-prototype.svg') as src:
    src = src.read()
    for name, date in DATES.items():
        output = OUTPUT.format(name)
        print('Writing to file:', output)
        with open(output, 'w') as dst:
            dst.write(src.format(DATE=date))
