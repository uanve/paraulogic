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
driver.refresh()
print(driver.title)

def input_paraula(mot):
    
    input_word = driver.find_element_by_id("test-word")
    driver.execute_script("arguments[0].innerText = '{}'".format(mot), input_word)

    enter = driver.find_element_by_id("submit-button")
    enter.click()

grid = driver.find_element_by_id("hex-grid")
lletres = grid.text.lower().split("\n")
lletra = lletres[3]

input_paraula("zonat")




import time
for mot in paraules_avui(lletres)[:]:
    print("provant ",mot)
    time.sleep(0.2)
    input_paraula(mot)
    
# driver.close()

        
        
    