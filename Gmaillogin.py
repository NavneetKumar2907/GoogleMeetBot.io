from selenium import webdriver
import selenium

from selenium.webdriver import ChromeOptions

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GmailLogin(object):
    """Login to gmail account.
    
    Attributes:
    
    _driver:

    
    Parameter:
    ...........................
    _email:
    _passw:
    """

    def __init__(self, email, passw):
        self._email = email
        self._passw = passw

        self._url = "https://www.gmail.com"

       


    def login(self):

        
        Cop = ChromeOptions()
        Cop.add_argument('use-fake-ui-for-media-stream')
        Cop.add_experimental_option('detach', True)
        Cop.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        

        self._driver = webdriver.Chrome(options= Cop, executable_path="chromedriver.exe")
        
        self._driver.get(self._url)
        eId = self._driver.find_element_by_name("identifier")
        eId.send_keys(self._email + Keys.ENTER)

        self._driver.implicitly_wait(5)
        # Wait till loaded
        passElem = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        passElem.send_keys(self._passw + Keys.ENTER)
        
        return self._driver