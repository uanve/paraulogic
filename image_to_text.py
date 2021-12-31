# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:17:52 2021

@author: joanv
"""

pip install pytesseract

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'C:/Users/joanv/OneDrive/Escritorio/Capture.png'))

text = pytesseract.image_to_string(r'C:/Users/joanv/OneDrive/Escritorio/Capture.png')

idx = text.find('paraules:') + 10

text = text[idx:]

text = text.replace('\n',' ')

text = text.split(', ')



dic = {' ':'', ',':'','à':'a', 'á':'a', '-':'', 'è':'e', 'é':'e', 'í':'i', 'ì':'i', 'ò':'o', 'ó':'o', 'ú':'u', 'ù':'u', 'ï':'i', '·':''}
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


for e in text:
    if len(e)<3:
        text.remove(e)
        
    elif ' o ' in e:
        print(e)
        text.remove(e)
        text.append(replace_all(e.split(' o ')[0],dic))
        
    elif '.' in e:
        print(e)
        text.remove(e)
        text.append(replace_all(e.split('.')[0],dic))
        
def words_in_image(image):
    text = pytesseract.image_to_string(r'{}'.format(image))
    
    idx = text.find('paraules:') + 10
    
    text = text[idx:]
    
    text = text.replace('\n',' ')
    
    text = text.split(', ')
    
    
    
    dic = {' ':'', ',':'','à':'a', 'á':'a', '-':'', 'è':'e', 'é':'e', 'í':'i', 'ì':'i', 'ò':'o', 'ó':'o', 'ú':'u', 'ù':'u', 'ï':'i', '·':''}
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    
    
    for e in text:
        if len(e)<3:
            text.remove(e)
            
        elif ' o ' in e:
            print(e)
            text.remove(e)
            text.append(replace_all(e.split(' o ')[0],dic))
            
        elif '.' in e:
            print(e)
            text.remove(e)
            text.append(replace_all(e.split('.')[0],dic))
            
    return text
        
words_in_image('C:/Users/joanv/OneDrive/Escritorio/Capture.png')
        


            
            
            

        


                                  