from selenium.webdriver.common.by import By

from PageObject import Locators

class SelectHotelPage:
    def __init__(self, driver):
        self.radio_btn=driver.find_element(By.ID, Locators.radio_id)
        self.continue_btn=driver.find_element(By.ID, Locators.continue_id)

    def getRadioBtn(self):
        return self.radio_btn

    def getContinueBtn(self):
        return self.continue_btn