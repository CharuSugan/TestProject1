from selenium.webdriver.common.by import By

from PageObject import Locators
from libglobal.LibGlobal import Base

class SearchHotelPage:
    def __init__(self, driver):
        self.dd_location=driver.find_element(By.ID, Locators.location_id)
        self.dd_hotels=driver.find_element(By.ID, Locators.hotels_id)
        self.dd_room_type=driver.find_element(By.ID, Locators.room_type_id)
        self.dd_number_rooms=driver.find_element(By.ID, Locators.number_room_id)
        self.txt_check_in=driver.find_element(By.ID, Locators.check_in_id)
        self.txt_check_out=driver.find_element(By.ID, Locators.check_out_id)
        self.dd_adults=driver.find_element(By.ID, Locators.adults_id)
        self.dd_child=driver.find_element(By.ID, Locators.child_id)
        self.btn_search=driver.find_element(By.ID, Locators.search_id)

    def getDDLocation(self):
        return self.dd_location

    def getDDHotels(self):
        return self.dd_hotels

    def getDDRoomType(self):
        return self.dd_room_type

    def getDDNumberRooms(self):
        return self.dd_number_rooms

    def getTxtCheckIn(self):
        return self.txt_check_in

    def getTxtCheckOut(self):
        return self.getTxtCheckOut()

    def getDDChild(self):
        return self.dd_child

    def getDDAdult(self):
        return self.dd_adults

    def getBtnSearch(self):
        return self.btn_search
