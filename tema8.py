'''
https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
https://www.jules.app

(obs: nu 3 pe fiecare pagina, 3 in total, de pe ce site doriti, la alegere. Nu toate sites vor avea elemente cu atributul name de ex)

3 selectors by:
Id
Link text
Partial link text
Name
Tag*
Class name*
Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

*La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista

La Xpath:
3 dupa atribut valoare
3 dupa textul de pe element
1 dupa partial text
1 cu SAU, folosind pipe |
1 cu *
1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
1 in care sa folosesti parent::
1 in care sa folosesti fratele anterior sau de dupa (la alegere)
1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.

Studiu extra daca doriti:
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
'''
#ID
chrome.get('http://automationpractice.com/index.php')
search_query_top=chrome.find_element(By.ID, 'search_query_top')
sleep(2)
search_query_top.send_keys('haine de firma')
sleep(2)

chrome.get('https://formy-project.herokuapp.com/autocomplete')
autocomplete=chrome.find_element(By.ID, 'autocomplete')
sleep(2)
autocomplete.send_keys('testare auto-complete')
sleep(2)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
datepicker=chrome.find_element(By.ID, 'datepicker')
sleep(2)
datepicker.send_keys('24/01/1987')
sleep(2)

# Link text

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'A/B Testing').click()
sleep(2)

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
sleep(2)

chrome.get('https://www.phptravels.net')
chrome.find_element(By.LINK_TEXT, 'Hotels').click()
sleep(2)

# Partial link text

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'A/B').click()
sleep(1)

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Add/Rem').click()
sleep(1)

chrome.get('https://www.phptravels.net')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Hote').click()
sleep(1)

# Name
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'firstname').send_keys('David')
sleep(5)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'lastname').send_keys('mondoc')
sleep(2)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'continents').send_keys('Europe')
sleep(2)

# Tag
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input')
print(len(lista_taguri))
lista_taguri[0].send_keys('testare0')
sleep(2)
lista_taguri[1].send_keys('testare1')
sleep(2)
lista_taguri[2].click()
sleep(2)
lista_taguri[3].click()
sleep(2)
lista_taguri[4].click()
sleep(2)
lista_taguri[5].click()
sleep(2)
lista_taguri[6].click()
sleep(2)
lista_taguri[7].click()
sleep(2)
lista_taguri[8].click()
sleep(2)
lista_taguri[9].click()
sleep(2)
lista_taguri[10].click()

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
lista_labels=chrome.find_elements(By.TAG_NAME, 'label')
print(len(lista_labels))
lista_labels[0].is_displayed()
lista_labels[1].is_displayed()
lista_labels[2].is_displayed()

chrome.get('http://automationpractice.com/index.php')
lista_form=chrome.find_elements(By.TAG_NAME, 'input')
print(len(lista_form))
lista_form[3].send_keys('testare automata')
sleep(1)
lista_form[4].send_keys('testare automata')
sleep(1)

#Class Name
# chrome.get('https://www.phptravels.net')
# chrome.find_elements(By.CLASS_NAME, "form-group")[0].click()
# sleep(2)
# chrome.find_elements(By.CLASS_NAME, "form-group")[1].click()
# sleep(2)
# chrome.find_elements(By.CLASS_NAME, "form-group")[2].click()
# sleep(2)
# chrome.find_elements(By.CLASS_NAME, "form-group")[3].click()
# sleep(2)

# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# lista_class=chrome.find_elements(By.CLASS_NAME, 'form-control' )
# print(len(lista_class))
# for i in range(len(lista_class)):
#     i=i+1
#     lista_class[i].send_keys('test')
#     sleep(5)

chrome.get('https://the-internet.herokuapp.com/hovers')
chrome.find_elements(By.CLASS_NAME, 'figure')[0].is_enabled()
chrome.find_elements(By.CLASS_NAME, 'figure')[1].is_enabled()
chrome.find_elements(By.CLASS_NAME, 'figure')[2].is_enabled()

# CSS
chrome.get ('https://the-internet.herokuapp.com/login')
# selector by CSS ID
chrome.find_element (By.CSS_SELECTOR , 'input#username').send_keys ('David')
sleep (2)

# selector by CSS - atribut=valoare
chrome.find_element (By.CSS_SELECTOR , 'input[id="password"]').send_keys ('testare parola atribut-valoare' )
sleep (2)

chrome.get('https://formy-project.herokuapp.com/autocomplete')
# selector by CSS - Class - only first one if multiple matches
chrome.find_element (By.CSS_SELECTOR , 'input.form-control').send_keys ('testare')
sleep (2)
'''
# XPath
# # 3 dupa atribut valoare
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

# chrome.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('oare merge?')
# sleep(3)

# chrome.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('dar asta merge?')
# sleep(3)

# chrome.find_element(By.XPATH, '//input[@id="sex-0"]').click()
# sleep(3)

# # 3 dupa textul de pe element
# chrome.get('http://automationpractice.com/index.php')
#
# chrome.find_element(By.XPATH, '//a[text()="Women"]').click()
# sleep(2)
#
# chrome.find_element(By.XPATH, '//b[text()="Cart"]').click()
# sleep(2)
#
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# chrome.find_element(By.XPATH, '//a[text()="Click here to Download File"]').click()
# sleep(2)

# # 1 cu SAU, folosind pipe |
# chrome.get('https://the-internet.herokuapp.com/login')
# s = chrome.find_element(By.XPATH, '//input[@name="Username"] | //input[@id="password"]')
# s.send_keys('test')
# sleep(5)

# # 1 cu *
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# chrome.find_element(By.XPATH, '//*[@type="text"]').send_keys('xxxxxxxxx')
# sleep(5)

# # 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
# chrome.get('https://www.phptravels.net/')
# chrome.find_element(By.XPATH, '//div[@class="col-md-6"][1]').click()
# sleep(5)

# # 1 in care sa folosesti parent:: - habar nu am daca am facut corect
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, '//input[@id="street_number"]/parent::div').is_enabled()
# sleep(5)
# # 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.XPATH, '//input[@id="street_number"]/following-sibling::input[@id="route"]').send_keys('mai multe teste')
sleep(5)

# # 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.






