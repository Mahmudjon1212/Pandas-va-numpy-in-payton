# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l8JqyRFRua2vt_DC4oW7kLSIPQ31RLcV
"""

import pandas as pd
baza= {
    "FISH":[ "MUhammadov Ozodbek" , "Mahmutaliyeva Iroda ", "Mamadaliyev Alimjon","Mahmudov Asliddin", "Kenjayev Bahodir","Nomozov Mahmudjon", "Nomozova Madina", "Nabiyev Bahrom", "Haydaraliyeva Barno", "Zaropov Habibullo"   ],
    "Manzili":[ "Toshloq ","Farg'ona ", "Farg'ona", "Qashqadaryo", "Farg'ona", "Farg'ona", "Farg'ona", "Farg'ona" , "Farg'ona","Chimyon" ],
    "Yoshi":[  "19 ","47", "29","19", "38","19","24","19","19","19" ],
    "Ish joyi":[ "Qurilish", "Palikilinika", "Maktab", "Qurilish" , "Fermer", "TATU_FF","FARDU","Palitexnika","Toshmiy", "TATU_FF"   ],
    "Jinsi":["Erkak","Ayol","Erkak","Erkak","Erkak","Erkak","Ayol","Erkak","Ayol","Erkak"],
}
db=pd.DataFrame(baza)
print(db)

filtr1=db[db["Yoshi"]=="19"]
print(filtr1)

filtr2=db[db["Yoshi"]>"19"]
print(filtr2)

filtr2=db[db["Jinsi"]=="Ayol"]
print(filtr2)