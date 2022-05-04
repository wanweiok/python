line = 'asdf fjdk; afed, fjek,asdf,   foo'
import re
res = re.split(r'[;,\s]\s*', line)
fields = re.split(r'(;|,|\s)\s*', line)
print(res)
print(fields)
print(fields[::2])
print(fields[1::2])

text1 = '11/27/2012'
date_pattern = re.compile(r'\d+/\d+/\d+')
if date_pattern.match(text1):
    print('yes')
else:
    print('no')

text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text2):
    print('{}-{}-{}'.format(month,day,year))

text3 = "hello world!"
print(text3.center(40, '='))
print(format(text3, '*^50'))

s = '{name} has {n} messages.'
name = "frank"
n = 20
print(s.format(name='Guido', n=37))
print(s.format_map(vars()))

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40, initial_indent='  '))

text = 'foo = 23 + 42 * 10'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
#scanner = master_pat.scanner('foo = 42')
def generate_tokens(pat, text):
    from collections import namedtuple
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)