import sys

str_ = sys.stdin.readline().rstrip()

happy = str_.count(':-)')
sad = str_.count(':-(')

if happy > sad: print('happy')
elif happy < sad: print('sad')
elif happy == sad and happy>0 and sad>0: print('unsure')
else: print('none')
