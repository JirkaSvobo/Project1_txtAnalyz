TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# ------------------------- text analysis -------------------------
txtAnalyse = {}

#for itm, tExt in enumerate(TEXTS, start=1):
#    txtList = tExt.strip(",.!?)(-").split(' ')
#    print(f'list {itm}, {txtList}')

tExt = TEXTS[0]
txtList = []
txtList = tExt.strip(",:/.!?)(-").split()
print(f'list var1: {txtList}')

dirty_words = tExt.split()
dirty_words.append('')
words = []
while dirty_words:
    word = dirty_words.pop()
    word = word.strip('.,:/;')
    words.append(word)
print(f'list var2a: {words}')

dirty_words2 = tExt.split()
dirty_words2.append('')
words2 = []
while dirty_words2:
    word = dirty_words2.pop()
    word = word.strip('.,:/;')
    if word: words2.append(word)
print(f'list var2b: {words2}')

setL1 = set(txtList)
setL2a = set(words)
setL2b = set(words2)

L1_L2a = setL1.symmetric_difference(setL2a)
L2a_L2b = setL2a.symmetric_difference(setL2b)

print(f'L1_L2a: {L1_L2a}')
print(f'L2a_L2b: {L2a_L2b}')