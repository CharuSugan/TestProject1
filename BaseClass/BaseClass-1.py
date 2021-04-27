from selenium.webdriver.common.by import By
from libglobal.LibGlobal import Base

class AdactinHotel(Base):

    def login(self):
        driver=self.browser_launch()
        driver.implicitly_wait(5)
        self.window_maximize()
        self.load_url("http://adactinhotelapp.com/index.php")
        txt_username=driver.find_element(By.ID, "username")
        self.send_input(txt_username, "Charumathi")
        txt_pwd=driver.find_element(By.ID, "password")
        self.send_input(txt_pwd, "appumeenu21$")
        btn_login=driver.find_element(By.ID, "login")
        self.btn_click(btn_login)

        loc=driver.find_element(By.ID, "location")
        self.index_select(loc, 2)

        hotels=driver.find_element(By.ID, "hotels")
        self.value_select(hotels, "Hotel Sunshine")

        room=driver.find_element(By.ID, "room_type")
        self.text_select(room, "Standard")

        room_count=driver.find_element(By.ID, "room_nos")
        self.value_select(room_count, "8")

        in_date=driver.find_element(By.ID, "datepick_in")
        self.send_input(in_date, "20/04/2021")

        out_date = driver.find_element(By.ID, "datepick_out")
        self.send_input(out_date, "22/04/2021")

        adult_room=driver.find_element(By.ID, "adult_room")
        self.index_select(adult_room, 3)

        child_room = driver.find_element(By.ID, "child_room")
        self.text_select(child_room, "4 - Four")

        search=driver.find_element(By.ID, "Submit")
        self.btn_click(search)

        radio=driver.find_element(By.ID, "radiobutton_0")
        self.btn_click(radio)

        Cont = driver.find_element(By.ID, "continue")
        self.btn_click(Cont)

        f_name=driver.find_element(By.ID, "first_name")
        self.send_input(f_name, "Charu")

        l_name = driver.find_element(By.ID, "last_name")
        self.send_input(l_name, "Gobi")

        address = driver.find_element(By.ID, "address")
        self.send_input(address, '''101, MG Road,
        Thuraipakkam,
        Chennai - 600097''')

        card_no = driver.find_element(By.ID, "cc_num")
        self.send_input(card_no, "1234567890123456")

        card_type=driver.find_element(By.ID, "cc_type")
        self.text_select(card_type, "American Express")

        expiry_month = driver.find_element(By.ID, "cc_exp_month")
        self.value_select(expiry_month, "8")

        expiry_year=driver.find_element(By.ID, "cc_exp_year")
        self.text_select(expiry_year, "2021")

        cvv=driver.find_element(By.ID, "cc_cvv")
        self.send_input(cvv, "123")

        book=driver.find_element(By.ID, "book_now")
        self.btn_click(book)

        order_no=driver.find_element(By.ID, "order_no")
        print(self.txt(order_no))

        self.screen_shot("BaseClass.png")



a=AdactinHotel()
a.login()

# class AdactinHotel:
#
#     def login(self):
#         b=Base()
#         driver=b.browser_launch()
#         driver.implicitly_wait(5)
#         b.window_maximize()
#         b.load_url("http://adactinhotelapp.com/index.php")
#         txt_username=driver.find_element(By.ID, "username")
#         b.send_input(txt_username, "Charumathi")
#         txt_pwd=driver.find_element(By.ID, "password")
#         b.send_input(txt_pwd, "appumeenu21$")
#         btn_login=driver.find_element(By.ID, "login")
#         b.btn_click(btn_login)
#
#         loc=driver.find_element(By.ID, "location")
#         b.index_select(loc, 2)
#
#         hotels=driver.find_element(By.ID, "hotels")
#         b.value_select(hotels, "Hotel Sunshine")
#
#         room=driver.find_element(By.ID, "room_type")
#         b.text_select(room, "Standard")
#
#         room_count=driver.find_element(By.ID, "room_nos")
#         b.value_select(room_count, "8")
#
#         in_date=driver.find_element(By.ID, "datepick_in")
#         b.send_input(in_date, "20/04/2021")
#
#         out_date = driver.find_element(By.ID, "datepick_out")
#         b.send_input(out_date, "22/04/2021")
#
#         adult_room=driver.find_element(By.ID, "adult_room")
#         b.index_select(adult_room, 3)
#
#         child_room = driver.find_element(By.ID, "child_room")
#         b.text_select(child_room, "4 - Four")
#
#         search=driver.find_element(By.ID, "Submit")
#         b.btn_click(search)
#
#         radio=driver.find_element(By.ID, "radiobutton_0")
#         b.btn_click(radio)
#
#         Cont = driver.find_element(By.ID, "continue")
#         b.btn_click(Cont)
#
#         f_name=driver.find_element(By.ID, "first_name")
#         b.send_input(f_name, "Charu")
#
#         l_name = driver.find_element(By.ID, "last_name")
#         b.send_input(l_name, "Gobi")
#
#         address = driver.find_element(By.ID, "address")
#         b.send_input(address, '''101, MG Road,
#         Thuraipakkam,
#         Chennai - 600097''')
#
#         card_no = driver.find_element(By.ID, "cc_num")
#         b.send_input(card_no, "1234567890123456")
#
#         card_type=driver.find_element(By.ID, "cc_type")
#         b.text_select(card_type, "American Express")
#
#         expiry_month = driver.find_element(By.ID, "cc_exp_month")
#         b.value_select(expiry_month, "8")
#
#         expiry_year=driver.find_element(By.ID, "cc_exp_year")
#         b.text_select(expiry_year, "2021")
#
#         cvv=driver.find_element(By.ID, "cc_cvv")
#         b.send_input(cvv, "123")
#
#         book=driver.find_element(By.ID, "book_now")
#         b.btn_click(book)
#
#         order_no=driver.find_element(By.ID, "order_no")
#         print(b.txt(order_no))