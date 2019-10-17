#BanglaTranslator_v1.0
#by Amlan Saha Kundu

import googletrans
from googletrans import Translator

print(" Welcome to Bengali Translator v1.0 by Amlan Saha Kundu")
translator = Translator()
try:
    f = open("English.txt","r", encoding="utf-8")
    g = open("Bengali.txt","w", encoding="utf-8")
    val = (f.read())
    translations = translator.translate( [str(val)], dest='bn')
    print("Translating....")
    for translation in translations:
        g.write(str(translation.text))
    g.close()
    print("Done")
    f.close()
except FileNotFoundError:
    print("\nSorry, No file is found to be translated in Bengali.\nPlease write something and save it in English.txt.\nThen, run the program.\n\nThank you.")
    open("English.txt","w", encoding="utf-8")
