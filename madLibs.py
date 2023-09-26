import re


verbRegex=re.compile(r'VERB')
nounRegex=re.compile(r'NOUN')
adjectiveRegex=re.compile(r'ADJECTIVE')
adverbRegex=re.compile(r'ADVERB')


def saisirRegex():
    a={}
    print('enter an adjective:')
    adjective=input()
    a.setdefault(adjective,adjectiveRegex)
    print('enter a noun:')
    noun=input()
    a.setdefault(noun,nounRegex)
    print('enter a verb:')
    verb=input()
    a.setdefault(verb,verbRegex)
    print('enter an adverb:')
    adverb=input()
    a.setdefault(adverb,adverbRegex)
    return a
regexdict=saisirRegex()
print(regexdict)
text='The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events,ADVERB.'
for k,v in regexdict.items():
    string=v.sub(k,text)
    text=string
print(text)
    

