# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:17:53 2021

@author: joanv
"""

import os
os.chdir("C:/Users/joanv/OneDrive/Escritorio/paraulogic_joc/paraulogic")


dic = {'à':'a', 'á':'a', '-':'', 'è':'e', 'é':'e', 'í':'i', 'ì':'i', 'ò':'o', 'ó':'o', 'ú':'u', 'ù':'u', 'ï':'i', '·':''}
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def paraules_avui(lletres):
    words = []
    with open('./paraules.txt', 'r') as f:
        for e in f:
            words.append(e[:-1])
            
    words_2 = []
    words_3 = []
    words_4 = []
    for word in words:
        word_2 = word.split(" ")[0]
        words_2.append(word_2)
        
        if word_2[-1] in "123456789":
            word_3 = word_2[:-1]
            
        else:
            word_3 = word_2[:]
        words_3.append(word_3)
        
    
    words_4 = []
    for e in words_3:
        if lletres[3] in e:
            words_4.append(e)
            
    abc = "abcdefghijklmnopqrstuvwxyzç"
    abc_today = ''.join(lletres)
    abc_not_today = ""
    for e in abc:
        if e not in abc_today:
            abc_not_today += e
    
    words_5 = []
    for e in words_4:
        if lletres[3] not in e:
            continue
        e_ = True
        for l in e:
            if l in abc_not_today:
                
                e_ = False
        if e_:
            e = replace_all(e,dic)
            words_5.append(e)
    
    return words_5
    




from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://paraulogic.rodamots.cat/")
# driver.refresh()
print(driver.title)