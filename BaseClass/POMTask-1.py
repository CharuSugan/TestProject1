from selenium import webdriver
from PageObject.Pages.LoginPage import LoginPage
from PageObject.Pages.SearchHotelPage import SearchHotelPage
from PageObject.Pages.SelectHotelPage import SelectHotelPage
from PageObject.Pages.BookHotelPage import BookHotelPage
from PageObject.Pages.BookingConfirmation import BookingConfirmation
from libglobal.LibGlobal import Base

class Sample(Base):

    # Login Page
    def login(self):
        self.driver=self.browser_launch()
        self.driver.implicitly_wait(10)
        self.load_url("http://adactinhotelapp.com/index.php")
        self.window_maximize()
        l=LoginPage(self.driver)
        self.send_input(l.txt_username, "Charumathi")
        self.send_input(l.txt_password, "appumeenu21$")
        self.btn_click(l.btn_login)

    # Search Hotel Page
    def searchHotel(self):
        s=SearchHotelPage(self.driver)
        self.index_select(s.dd_location, 2)
        self.value_select(s.dd_hotels, "Hotel Creek")
        self.text_select(s.dd_room_type, "Double")
        self.index_select(s.dd_number_rooms, 5)
        self.send_input(s.txt_check_in, "22/04/2021")
        self.send_input(s.txt_check_out, "23/04/2021")
        self.index_select(s.dd_adults, 2)
        self.index_select(s.dd_child, 2)
        self.btn_click(s.btn_search)

    # Select Hotel Page
    def selectHotel(self):
        sh=SelectHotelPage(self.driver)
        self.btn_click(sh.radio_btn)
        self.btn_click(sh.continue_btn)

    # Book Hotel Page
    def bookHotel(self):
        b=BookHotelPage(self.driver)
        self.send_input(b.txt_first_name, "Charu")
        self.send_input(b.txt_last_name, "Mathi")
        self.send_input(b.txt_address, "Chennai")
        self.send_input(b.txt_cc_num, "1234567890123456")
        self.text_select(b.dd_cc_type, "VISA")
        self.index_select(b.dd_exp_moth, 8)
        self.value_select(b.dd_exp_year, "2021")
        self.send_input(b.txt_cvv_num, "456")
        self.btn_click(b.btn_book_now)

    # Booking Confirmation
    def bookingConfirmation(self):
        bc=BookingConfirmation(self.driver)
        order_no=self.txt(bc.txt_order_no)
        print(order_no)
        self.screen_shot("BookingConfirmation.png")


s=Sample()
s.login()
s.searchHotel()
s.selectHotel()
s.bookHotel()
s.bookingConfirmation()

