from Gmaillogin import *

class Meet(object):
    """To join Meet"""

    def __init__(self, email,passw,url):
        
        self._url = url
        self._gmail = GmailLogin(email=email, passw=passw)


    
    def Join(self):
        self._driver = self._gmail.login()
        self._driver.get(self._url)
        self._driver.refresh()
        self._driver.implicitly_wait(5)
        self._driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'d')
        self._driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'e')
        # Join using class name
        try:
            self._driver.find_element_by_class_name('NPEfkd').click()
        except:
             
            self._driver.find_element_by_class_name('RveJvd').click()
        finally:
            
            self._driver.find_element_by_class_name('snByac').click()
        


