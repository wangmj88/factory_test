x = 'ABC'
l = [i for i in x]
print(l)

dummy = [ord(x) for x in x]
print (dummy)

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s)> 127]
print(beyond_ascii)

beynod_ascii = list(filter(lambda c:c > 127,map(ord,symbols)))
print(beyond_ascii)

colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color , size)  for color in colors for size in sizes ]
print(tshirts)

for color in colors:
    for size in sizes:
        print(color,size)


tshirts = [(size,color) for size in sizes
                        for color in colors]

print(tshirts)

symbols = '$¢£¥€¤'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

#使用生成器表达式计算笛卡尔积
colors = ['black','white']
sizes = ['S','M','L']

for tshirts in ('%s  %s' %(c,s) for s in sizes
                            for c in colors):
    print(tshirts)

print(divmod(20, 8))

a,b,*rest = range(5)
print(a)
print(b)
print(rest)

from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('tokyo','jp',36.933,(35.689722,139.691667))
print(tokyo)
print(tokyo[1])

print(City._fields)
LatLong = namedtuple('LatLong','lat long')

a =(1,2,3,2,(3,4,5))
b = (3,4,5)
print(a + b)
print(a.__contains__(b))
print(a.count(2))
print(a.__getitem__(2))
print(a.index(2))
print(a.__mul__(2))
print(b.__rmul__(2))

s = 'bicycle'
print(s)
print(s[::-1])
print(s[::-2])
print(s[::2])

invoice = """
... 0.....6................................40........52...55........
...	1909 Pimoroni PiBrella	    $17.50	3	$52.50
...	1489 6mm Tactile Switch x20	$4.95	2	$9.90
...	1510 Panavise Jr. - PV-201	$28.00	1	$28.00
...	1601 PiTFT Mini Kit 320x240	$34.95	1	$34.95
...	"""

SKU = slice(0,6)
print(SKU)
DESCRIPTION = slice(6, 40)
print(DESCRIPTION)
UNIT_PRICE = slice(40, 52)
print(UNIT_PRICE)
QUANTITY = slice(52, 55)
print(QUANTITY)
ITEM_TOTAL = slice(55, None)
print(ITEM_TOTAL)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE])

board = [['_']*3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)


