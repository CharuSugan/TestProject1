import time
from PageObject.Pages.LoginPage import LoginPage
from PageObject.Pages.SearchHotelPage import SearchHotelPage
from PageObject.Pages.SelectHotelPage import SelectHotelPage
from PageObject.Pages.BookHotelPage import BookHotelPage
from PageObject.Pages.BookingConfirmation import BookingConfirmation
from libglobal.LibGlobal import Base

from PageObject.Pages.DemoRegPage import DemoRegPage
class Sample(Base):
    def register(self):
        self.driver=self.browser_launch()
        self.window_maximize()
        self.load_url("http://demo.automationtesting.in/Register.html")
        d=DemoRegPage(self.driver)

        self.driver.implicitly_wait(20)
        r=self.get_max_row()
        print("Row:", r)
        c=self.get_max_col()
        print("Column:", c)
        self.send_input(d.txt_demo_first_name, self.get_data_from_excel(1, 2, "Demo"))
        self.send_input(d.txt_demo_last_name, self.get_data_from_excel(2, 2, "Demo"))
        self.send_input(d.txt_demo_address, self.get_data_from_excel(3, 2, "Demo"))
        self.send_input(d.txt_demo_email, self.get_data_from_excel(4, 2, "Demo"))
        self.send_input(d.txt_demo_phone, self.get_data_from_excel(5, 2, "Demo"))
        self.btn_click(d.dd_demo_gender_female)
        self.btn_click(d.check_demo_movies)
        self.btn_click(d.txt_language)
        self.btn_click(d.txt_demo_lang_select)
        self.text_select(d.dd_demo_skills, self.get_data_from_excel(9, 2, "Demo"))
        self.text_select(d.dd_demo_country, self.get_data_from_excel(10, 2, "Demo"))
        self.text_select(d.dd_demo_select_country, self.get_data_from_excel(11, 2, "Demo"))
        self.index_select(d.dd_demo_year, 50)
        self.text_select(d.dd_demo_month, self.get_data_from_excel(13, 2, "Demo"))
        self.index_select(d.dd_demo_date, 20)
        self.send_input(d.txt_demo_pwd, self.get_data_from_excel(15, 2, "Demo"))
        self.send_input(d.txt_demo_confirm_pwd, self.get_data_from_excel(16, 2, "Demo"))
        self.btn_click(d.btn_demo_submit)



s=Sample()
s.register()





