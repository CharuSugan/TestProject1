from selenium.webdriver.common.by import By

from PageObject import Locators

class BookHotelPage:
    def __init__(self, driver):
        self.txt_first_name=driver.find_element(By.ID, Locators.first_name_id)
        self.txt_last_name=driver.find_element(By.ID, Locators.last_name_id)
        self.txt_address=driver.find_element(By.ID, Locators.address_id)
        self.txt_cc_num=driver.find_element(By.ID, Locators.cc_num_id)
        self.dd_cc_type=driver.find_element(By.ID, Locators.cc_type_id)
        self.dd_exp_moth=driver.find_element(By.ID, Locators.cc_exp_month_id)
        self.dd_exp_year=driver.find_element(By.ID, Locators.cc_exp_year_id)
        self.txt_cvv_num=driver.find_element(By.ID, Locators.cc_cvv_id)
        self.btn_book_now=driver.find_element(By.ID, Locators.book_now_id)

    def getFirstName(self):
        return self.txt_first_name

    def getLastName(self):
        return self.txt_last_name

    def getAddress(self):
        return self.txt_address

    def getCCNumber(self):
        return self.txt_cc_num

    def getCCType(self):
        return self.dd_cc_type

    def getExpyMonth(self):
        return self.dd_exp_moth

    def getExpyYear(self):
        return self.dd_exp_year

    def getCVVNumber(self):
        return self.txt_cvv_num

    def getBookNow(self):
        return self.btn_book_now
