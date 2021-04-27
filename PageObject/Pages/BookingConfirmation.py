from selenium.webdriver.common.by import By

from PageObject import Locators

class BookingConfirmation:
    def __init__(self, driver):
        self.txt_order_no=driver.find_element(By.ID, Locators.order_no_id)

    def getOrderNumber(self):
        return self.txt_order_no