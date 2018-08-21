from collections import Counter
from googletrans import Translator
import requests
from googletrans import Translator


translator = Translator()
def Translate(arr):
    rus = []
    eng = []
    for i in arr:
        try:
            translation = translator.translate(i, dest='ru')
            eng.append(translation.origin)
            rus.append(translation.text)
            print(translation.origin, ' -> ', translation.text)
        except:
            pass
        



translator = Translator()
print('input path to your book:')
path = input()
f = open(path, 'r')
text = f.read()
division = []
for i in text:
    if not (i.isalpha() or i =="'"):
        division.append(i)

for i in division:
    text = text.replace(i,' ')
text = text.lower()
array = text.split()

unique = []
for i in array:
   if array.count(i) == 1:
       unique.append(i)
print(len(unique))
unique.sort()
Translate(unique)
