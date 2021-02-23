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

users = dict(bob='123', ann='pass123', mike='password123', liz='pass123')
oddelovac = 40*'-'

userNam = 'bob' #str(input('username: '))
passwd = '123' # str(input('password: '))

if userNam not in users.keys() or passwd != users[userNam]:
    print('either user name or password is incorrect')
    exit()

print(f'''username: {userNam}
password: {passwd}
{oddelovac}
Welcome to the app, {userNam}
We have 3 texts to be analyzed.
{oddelovac}''')
txtSelect = 1 #int(input('Enter a number btw. 1 and 3 to select text: '))
print(oddelovac)

if txtSelect not in range(1,len(TEXTS)+1):
    print('you selected wrong text ID')
    exit()


txtList = TEXTS[txtSelect-1].strip(",.!?)(-").split(' ')
txtAnalyze = {}
txtAnalyze[f'Text{txtSelect}'] = {'numberOfWords' : sum(1 for iTem in txtList if not iTem.isdecimal()),
                                  'titlecaseWords' : sum(1 for iTem in txtList if iTem.istitle()),
                                  'uppercaseWords' : sum(1 for iTem in txtList if iTem.isupper()),
                                  'lowercase words': sum(1 for iTem in txtList if iTem.islower()),
                                  'numeric strings' : sum(1 for iTem in txtList if iTem.isdecimal()),
                                  'sumOfNumbers' : sum(int(iTem) for iTem in txtList if iTem.isdecimal()),
                                  'wordOccurrence' : {iTem : txtList.count(iTem) for iTem in txtList}}

wordLengthOccurrence = {}
for item in txtList:
    wordLengthOccurrence.setdefault(len(item), 0)
    wordLengthOccurrence[len(item)] += 1

txtAnalyze[f'Text{txtSelect}'].update({'wordLengthOccurrence' : wordLengthOccurrence})

print(f'''
- počet slov je: {txtAnalyze[f'Text{txtSelect}']['numberOfWords']},
- počet slov začínajících velkým písmenem je: {txtAnalyze[f'Text{txtSelect}']['titlecaseWords']},
- počet slov psaných velkými písmeny je: {txtAnalyze[f'Text{txtSelect}']['uppercaseWords']},
- počet slov psaných malými písmenyje: {txtAnalyze[f'Text{txtSelect}']['lowercase words']},
- počet čísel (ne cifer)je: {txtAnalyze[f'Text{txtSelect}']['numeric strings']},
- sumu všech čísel (ne cifer) v textuje: {txtAnalyze[f'Text{txtSelect}']['sumOfNumbers']}.
''')


print(TEXTS[txtSelect-1])
print(sorted(wordLengthOccurrence.items())[2], '==', len(sorted(wordLengthOccurrence.items())))
print(txtAnalyze)