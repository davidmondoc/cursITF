# Implementati o clasa Login care sa mosteneasca unittest.TestCase
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login(TestCase):
# Gasiti elementele in partea de sus folosind ce selectors doriti voi
    LOGIN_BTN=(By.XPATH, '//*[@id="login"]/button')
    H2_TEXT=(By.XPATH, '//*[@id="content"]/div/h2')
    ATTR_CHECK=(By.XPATH, '//*[@id="page-footer"]/div/div/a')
    ERROR.MESSAGE=()
# setUp()
    def setUp(self):
# Driver
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome (service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
# https://the-internet.herokuapp.com/
        self.chrome.get('https://the-internet.herokuapp.com/')
# Click pe Form Authentication
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.sleep(4)

# tearDown()
# Quit browser
    def tearDown(self):
        self.chrome.quit()

# Test1
# Verificati ca noul url e corect
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'URL is incorrect')

# Test2
# Verificati ca page title e corect
    def test_page_title(self):
        actual = self.chrome.title
        print(f"Titlul extras al paginii este {actual}")
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

# Test3
# Verificati textul de pe elementul xpath=//h2 e corect
    def test_element_text(self):
        actual = self.chrome.find_element(*self.H2_TEXT).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'h2 text incorect')

# Test4
# Verificati ca butonul de login este displayed
    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.LOGIN_BTN)
        self.assertTrue(elem.is_displayed(), 'buton log-in nu e vizibil')

# Test5
# Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect
    def test_elem_atribute(self):
        actual = self.chrome.find_element(*self.ATTR_CHECK).get_attribute('class')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'atributul href al linkului Elemental Selenium nu e corect ')

# Test6
# Lasati goale user si pass
# Click login
    def user_pass(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()
# Verifica ca eroarea e displayed
        error=self.chrome.find_element(*self.ERROR.MESSAGE)
        self.assertTrue(error.is_displayed(), 'apare mesajul de eroare la logare')
#
# Test7
# Completeaza cu user si pass invalide
# Click login
# Verifica ca mesajul de pe eroare e corect
# Este si un x pus acolo extra asa ca vom folosi solutia de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is incorrect')