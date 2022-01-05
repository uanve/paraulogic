dic = {'à':'a', 'á':'a', 'č':'c','-':'', 'è':'e', 'é':'e', 'í':'i', 'ì':'i', 'ò':'o', 'ó':'o', 'ú':'u', 'ù':'u', 'ï':'i', '·':'',"'":'', '&':'', '/':'','-':'', '+':'', \
    'ñ':'', '1':'', '2':'', '3':'', '4':'', '5':'', ';':'', 'ü':'u', '.':''}
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


import io
f = open("catalan_words.txt",'r',encoding='utf8')
f_clean = open("catalan_words_clean.txt",'w',encoding='utf8')
for w in f:
    w = w[:-1]
    if len(w.split(" "))>1:
        pass
    else:
        w = w.lower()
        w = replace_all(w,dic)
        if len(w)>=3:
            f_clean.write(w+"\n")
f.close()
f_clean.close()
