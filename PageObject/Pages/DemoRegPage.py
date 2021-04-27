from selenium.webdriver.common.by import By
from PageObject import Locators

class DemoRegPage:
    def __init__(self, driver):
        self.txt_demo_first_name=driver.find_element(By.XPATH, Locators.demo_txt_first_name_xpath)
        self.txt_demo_last_name=driver.find_element(By.XPATH, Locators.demo_txt_last_name_xpath)
        self.txt_demo_address=driver.find_element(By.XPATH, Locators.demo_txt_address_xpath)
        self.txt_demo_email=driver.find_element(By.XPATH, Locators.demo_txt_email_xpath)
        self.txt_demo_phone=driver.find_element(By.XPATH, Locators.demo_txt_phone_xpath)
        self.dd_demo_gender_male=driver.find_element(By.XPATH, Locators.demo_radio_male_xpath)
        self.dd_demo_gender_female=driver.find_element(By.XPATH, Locators.demo_radio_female_xpath)
        self.check_demo_cricket=driver.find_element(By.ID, Locators.demo_check_cricket_id)
        self.check_demo_movies=driver.find_element(By.ID, Locators.demo_check_movies_id)
        self.check_demo_hockey=driver.find_element(By.ID, Locators.demo_check_hockey_id)
        self.txt_language=driver.find_element(By.ID, Locators.demo_language_id)
        self.txt_demo_lang_select=driver.find_element(By.XPATH, Locators.demo_txt_lang_select_xpath)
        self.dd_demo_skills=driver.find_element(By.ID, Locators.demo_dd_skills_id)
        self.dd_demo_country=driver.find_element(By.ID, Locators.demo_dd_country_id)
        self.dd_demo_select_country=driver.find_element(By.ID, Locators.demo_dd_select_country_id)
        self.dd_demo_year=driver.find_element(By.ID, Locators.demo_dd_year_id)
        self.dd_demo_month=driver.find_element(By.XPATH, Locators.demo_dd_month_xpath)
        self.dd_demo_date=driver.find_element(By.ID, Locators.demo_dd_date_id)
        self.txt_demo_pwd=driver.find_element(By.ID, Locators.demo_txt_password_id)
        self.txt_demo_confirm_pwd=driver.find_element(By.ID, Locators.demo_txt_confirm_pwd_id)
        self.btn_demo_submit=driver.find_element(By.ID, Locators.demo_btn_submit_id)

    def getDemoTxtFirstName(self):
        return self.txt_demo_first_name

    def getDemoTxtLastName(self):
        return self.txt_demo_last_name

    def getDemoTxtAddress(self):
        return self.txt_demo_address

    def getDemoTxtPhone(self):
        return self.txt_demo_phone

    def getDemoTxtEmail(self):
        return self.txt_demo_email

    def getDemoRadioGenderMale(self):
        return self.dd_demo_gender_male

    def getDemoRadioGenderFemale(self):
        return self.dd_demo_gender_female

    def getDemoCheckCricket(self):
        return self.check_demo_cricket

    def getDemoCheckMovies(self):
        return self.check_demo_movies

    def getDemoCheckHockey(self):
        return self.check_demo_hockey

    def getLanguage(self):
        return self.txt_language

    def getDemoTxtLanguage(self):
        return self.txt_demo_lang_select

    def getDemoDDSkills(self):
        return self.dd_demo_skills

    def getDemoDDCountry(self):
        return self.dd_demo_country

    def getDemoDDSelectCountry(self):
        return self.dd_demo_select_country

    def getDemoDDYear(self):
        return self.dd_demo_year

    def getDemoDDMonth(self):
        return self.dd_demo_month

    def getDemoDDDate(self):
        return self.dd_demo_date

    def getDemoTxtPwd(self):
        return self.txt_demo_pwd

    def getDemoTxtConfirmPwd(self):
        return self.txt_demo_confirm_pwd

    def getDemoBtnSubmit(self):
        return self.btn_demo_submit



