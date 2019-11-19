#BanglaTranslator_v1.0.1
#by Amlan Saha Kundu
#edited by debojyoti Chakraborty

import googletrans
import sys
import time
from googletrans import Translator

print(" Welcome to Bengali Translator v1.0.1 by Amlan Saha Kundu")
print('start editing by debojyoti Chakraborty')
s=time.time()*1000
f=sys.argv[1]

 

translator = Translator()
try:
   
    with open(f,'r') as f:
        val = (f.read())
        translations = translator.translate( [str(val)], dest='bn')
        print("Translating....")
        with open('new'+str(s)+'ben'+'.txt','w') as g:
            for translation in translations:
                g.write(str(translation.text))
            g.close()
        print("Done")
        f.close()
except FileNotFoundError:
    print("\nSorry, No file is found to be translated in Bengali.\nPlease write something and save it in English.txt.\nThen, run the program.\n\nThank you.")

