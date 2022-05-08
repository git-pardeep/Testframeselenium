from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basedriver():
    def __init__(self,driver):
        self.driver=driver
    def element_to_be_clickable(self,locator_type,locator_path):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.element_to_be_clickable((locator_type,locator_path)))
    def presence_elements(self,locator_type,locator_path):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_all_elements_located((locator_type,locator_path)))



