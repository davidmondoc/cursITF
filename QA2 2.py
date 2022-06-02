#IMPLICIT WAIT
# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# setam implicit wait in secunde
# selenium va cauta toate elementele timp de x secunde inainte sa dea eroare
chrome.implicitly_wait(1)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# elem gasit
chrome.find_element(By.ID, 'first-name').send_keys('Andy')

# id e invalid => NoSuchElementException
chrome.find_element(By.ID, 'last-name123').send_keys('Andy')

# de citit
# https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/

#EXPLICIT WAIT

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# setam implicit wait in secunde
# selenium va cauta toate elementele timp de x secunde inainte sa dea eroare
chrome.implicitly_wait(10)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# elem gasit
chrome.find_element(By.ID, 'first-name').send_keys('Andy')

# cauta elementul timp de 10 secunde
last_name = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.ID, "last-name123")))
last_name.send_keys('S')

# https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/

#ASSERT 1

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

# chrome.get('https://formy-project.herokuapp.com/form')

# actual = chrome.current_url
# expected = 'https://formy-project.herokuapp.com/form'

chrome.get("https://formy-project.herokuapp.com/")
sleep(1)
chrome.find_element(By.LINK_TEXT,"Autocomplete").click()
sleep(1)
actual = chrome.current_url
expected = "https://formy-project.herokuapp.com/autocomplete"
sleep(1)
chrome.find_element(By.ID,"autocomplete").send_keys("Strada micsunelelor")
sleep(1)
assert actual == expected, f'INVALID URL: expected {expected} but found {actual}'

print('TEST PASSED')

# ASSERT 2
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()


chrome.get("https://jules.app/sign-in")
sleep(2)
actual_text = chrome.find_element(By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[3]/button").text
# element = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[3]/button")))
sleep(1)
expected_text = "LOG IN"
sleep(1)
assert actual_text == expected_text, f'INVALID Text: expected {expected_text} but found {actual_text}'

print('TEST PASSED')

#UNITTEST

# import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(TestCase):
    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    SUBMIT_BTN = (By.XPATH, '//a[@role="button"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//input[@id="middle-name"]')

    # se rulaza inainte de fiecare test si are rolul de a face setupul de chrome inainte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    # se ruleaza dupa fiecare test si are rolul de a inchide driver-ul de chrome dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # # verificam URL
    # def test_url(self):
    #     actual = self.chrome.current_url
    #     expected = 'https://formy-project.herokuapp.com/form'
    #     # expected value, actual value, mesaj in caz de fail
    #     self.assertEqual(expected, actual, 'URL is incorrect')

    # # verificam page title
    # def test_page_title(self):
    #     actual = self.chrome.title # se extrage automat titlul paginii incarcate prin intermediul metodei title
    #     print(f"Titlul extras al paginii este {actual}")
    #     expected = 'Formy'
    #     self.assertEqual(expected, actual, 'Page title is incorrect')
    #
    # # verificam text de pe element (buton, mesaj de eroare etc)
    # def test_submit_btn_text(self):
    #     # * tuple unpacking - se ia valoarea din tuple si se da ca argument in functie
    #     actual = self.chrome.find_element(*self.SUBMIT_BTN).text
    #     expected = 'Submit'
    #     self.assertEqual(expected, actual, 'Submit btn text is incorrect')
    #
    # # verificam ca element e vizibil
    # def test_elem_visible(self):
    #     elem = self.chrome.find_element(*self.SUBMIT_BTN)
    #     self.assertTrue(elem.is_displayed(), 'Submit btn nu e vizibil')
    #
    # # verificam ca element are un atribut asteptat (ex clasa)
    # def test_elem_atribute(self):
    #     actual = self.chrome.find_element(*self.SUBMIT_BTN).get_attribute('class')
    #     expected = 'btn btn-lg btn-primary'
    #     self.assertEqual(expected, actual, 'Submit btn href attribute is wrong')
    #
    #
    # # verificam ca element nu e prezent
    # def test_elem_not_displayed(self):
    #     # ai zice ca merge asa dar nu
    #     # middle_name = self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
    #     # self.assertFalse(middle_name.is_displayed(), 'Mid name e vizibil')
    #     pass

    # verificam ca element nu e prezent v1
    # def test_elem_not_displayed_v1(self):
    #     # verificam ca lista e goala
    #     middle_name = self.chrome.find_elements(*self.MIDDLE_NAME_INPUT)
    #     self.assertTrue(len(middle_name) > 0, 'Mid name e vizibil in mod incorect')
    #
    # # verificam ca element nu e prezent v2
    # def test_elem_not_displayed_v2(self):
    #     # verificam ca apare exceptia NoSuchElementException
    #     try:
    #         self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
    #     except NoSuchElementException:
    #         print("elementul nu se afla pe pagina, este ok")

    # waits pe url
    def test_url_waits(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        # asteptam ca fostul url sa se schimbe
        print(self.chrome.current_url)
        WebDriverWait(self.chrome, 5).until(EC.url_changes('https://formy-project.herokuapp.com/form'))
        # asteptam ca noul url sa contina
        WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        # asteptam ca noul url sa fie exact
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://formy-project.herokuapp.com/thanks'))

        # daca in 5 secunde nu ajungem pe url corect putem
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')

# cautare pe site dupa parent:: /preceding-sibling:: /following-sibling::
# //div[@class="form-group"]/parent::form/div/div[4]/div[2]/input/parent::div/preceding-sibling::div/following-sibling::div

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test2(unittest.TestCase):
    # elementele din pagina se pot gasi in partea de sus
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    CONTACT_US = (By.XPATH, '//a[text()="Contact us"]') # se scrie in tuple pt ca e imutabil()cums e scrie asa ramane
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submitMessage"]')
    ERROR_MESSAGE = (By.XPATH, '//ol/li')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('http://automationpractice.com/index.php') #url de start
        self.chrome.implicitly_wait(10)
        # se gaseste un element-> se da click pe el"contact us->ajungem pe un nou url
        self.chrome.find_element(*self.CONTACT_US).click()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'http://automationpractice.com/index.php?controller=contact'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Contact us - My Store'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_elem_visible(self):
        self.chrome.find_element(*self.SUBMIT_BUTTON).click() #dam click pe buton
        error = self.chrome.find_element(*self.ERROR_MESSAGE) #salvam eroarea ca element(eroarea)
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila') #afisam mai jos ca exista eroarea