from Negative.labirint_2 import MainPage_negative

from pages.labirint import MainPage_help
from pages.labirint import MainPage
from pages.labirint import MainPage_story
from pages.labirint import MainPage_cost
from pages.labirint_1 import MainPage_down
from pages.labirint import MainPage_book
from pages.labirint import MainPage_change_book

import time

#Нужна немнго добваить время,а иначе не получится (очень важно, не больше 2 сек !!!)!


#работает негативный тест часть 2
# иностранные слова
def test_negative_1(web_browser):
   page = MainPage_negative(web_browser)
   page.search = 'aksdnkjnadjknkjanda'
   page.search_run_button.click()
   # набор цифр


def test_negative_2(web_browser):
   page = MainPage_negative(web_browser)
   page.search = '6798996896867897968987'
   page.search_run_button.click()
   # Набор слов


def test_negative_3(web_browser):
   page = MainPage_negative(web_browser)
   page.search = 'ПРВАПАЛОПТУЦПУОУЦПОЛДАЦКОУПЛОО'
   page.search_run_button.click()
   # Максимальное набор слов, числ , иностраннные слов


def test_negative_4(web_browser):
   page = MainPage_negative(web_browser)
   page.search = ' FGHDFGDHWGHKWGИПРАЛОРВАЛОЛРЛПРЛОПРАВПЬТ9876978507859068756975687895679879678569804868707868950785699'
   page.search_run_button.click()
   # пустое значение


def test_negative_5(web_browser):
   page = MainPage_negative(web_browser)
   page.search = ''
   page.search_run_button.click()
   # спецсимволы


def test_negative_6(web_browser):
   page = MainPage_negative(web_browser)
   page.search = '!!!!!!!!!@%#$$^%$^$@$%$@%%@%$%$$#%$%%^&'
   page.search_run_button.click()

#работает негатив часть 2.1
#я так решил смогу зарег без кода
def test_middle_move(web_browser):
   page=MainPage_negative(web_browser)
   page.search_written=('jrjwneqnfnkjqerjwfmewrfmkfwekfkwm rmklmmmkjmnknkjnbhjbhgvfvhbghg@mail.ru')
   page.search_written.click()
   time.sleep(3)
   page.searchreport.click()
   #немного усложняю
def test_middle_move_1(web_browser):
   page = MainPage_negative(web_browser)
   page.search_written = ('jrjwneqnfnkjqerjwfmewrfmkfwekfkwm rmklmmmkjmnknkjnbhjbhgvfvhbghg@mail.ru')
   page.search_written.click()
   time.sleep(3)
   page.search = 'Пушкин'
   page.search_run_button.click()
   page.sort_table.click()
   all_prices = page.product_cost.get_text()
   all_prices = [float(p.replace(' ', '')) for p in all_prices]
   assert all_prices == sorted(all_prices)

  # еще сложнее(не поверил логин (просит указать_ааха)

def test_middle_move_1(web_browser):
   page = MainPage_negative(web_browser)
   page.search_written = ('jrjwneqnfnkjqerjwfmewrfmkfwekfkwm rmklmmmkjmnknkjnbhjbhgvfvhbghg@mail.ru')
   page.search_written.click()
   time.sleep(3)
   page.search = 'Пушкин'
   page.search_run_button.click()
   page.sort_table.click()
   all_prices = page.product_cost.get_text()
   all_prices = [float(p.replace(' ', '')) for p in all_prices]
   assert all_prices == sorted(all_prices)
   page.Try_bye.is_clickable()
   page.Try_bye.click()
   page.Try_bye_check.click()

def test_change_page(web_browser):
   page = MainPage_negative(web_browser)
   page.search = 'Гоголь'
   page.search_run_button.click()
   page.button.click()
   page.search_run_button_down = 'Эдгар По'
   page.search_run_button_down.click()
   page.subject.click()
   time.sleep(2)
   page.sort_table.click()


#Работает часть 1
def test_simple_eighteen(web_browser):
    page=MainPage(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
def test_book_cost_2(web_browser):
   page = MainPage_cost(web_browser)
   page.search = 'Лев Николай Толстой'
   page.search_run_button.click()
   page.Author.click()
   page.deal.click()
   time.sleep(5)
   page.reviews.click()
   page.video.click()
   page.newspaper.click()
def test_book_cost_2(web_browser):
   page = MainPage_cost(web_browser)
   page.search = 'Лермотов'
   page.search_run_button.click()
   page.Author.click()
   page.Authour_Lermotov.click()
   page.sort_table_1.click()
   all_prices = page.product_cost.get_text()
   all_prices = [float(p.replace(' ', '')) for p in all_prices]
   assert all_prices == sorted(all_prices)

def test_book_cost_1(web_browser):
   page = MainPage_cost(web_browser)
   page.search = 'Пушкин'
   page.search_run_button.click()
   page.sort_table.click()
   all_prices = page.product_cost.get_text()
   all_prices = [float(p.replace(' ', '')) for p in all_prices]
   assert all_prices == sorted(all_prices)

#простое и популяроное значение
def test_lab(web_browser):
   page = MainPage(web_browser)
   page.search = 'книги'
   page.search_run_button.click()
#Значение временное но популярное
def test_search_story_value(web_browser):
   page = MainPage_story(web_browser)
   page.search = "Достоевский"
   page.search_run_button.click()
   page.search_book_bye_1.click()
   page.search_book_check.click()
#Находим конкретно !
def test_search_story_1(web_browser):
   page = MainPage_story(web_browser)
   page.search = "Федор Достовкий престпуление и наказние"
   page.search_run_button.click()
   page.search_book_bye_2.click()


# конкертный и популярный  жанр
def test_lab_founded(web_browser):
   page = MainPage(web_browser)
   page.search = 'Детектив'
   page.search_run_button.click()


def test_lab_founded_travel(web_browser):
   page = MainPage(web_browser)
   page.search = 'сказка'
   page.search_run_button.click()


def test_lab_founded_travel(web_browser):
   page = MainPage(web_browser)
   page.search = 'путешествие '
   page.search_run_button.click()

#работает часть 1.2
def test_down_1(web_browser):
   page = MainPage_down(web_browser)
   page.overlap.find()
   page.apple.click()
   page.wait_page_loaded()
   time.sleep(1)
def test_down_2(web_browser):
   page = MainPage_down(web_browser)
   page.overlap.find()
   page.google.click()
   page.wait_page_loaded()
   time.sleep(1)
def test_down_3(web_browser):
   page = MainPage_down(web_browser)
   page.overlap.find()
   page.apple_gallery.click()
   page.wait_page_loaded()
   time.sleep(1)
#работа 1 часть 1.3 меню.

def test_club(web_browser):
   page = MainPage_book(web_browser)
   page.book.click()
def test_club(web_browser):
   page = MainPage_book(web_browser)
   page.club.click()
def test_numberone(web_browser):
   page=MainPage_book(web_browser)
   page.number_one.click()

def test_shool(web_browser):
   page=MainPage_book(web_browser)
   page.school.click()
def test_games(web_browser):
   page=MainPage_book(web_browser)
   page.playgame.click()
def test_club(web_browser):
   page = MainPage_book(web_browser)
   page.place.click()
def test_develery(web_browser):
   page = MainPage_book(web_browser)
   page.develery.click()
   time.sleep(1)

# Работа часть 1.4 под меню
def test_costpay(web_browser):
   page = MainPage_book(web_browser)
   page.cost_pay.click()
   time.sleep(1)
def test_sertif(web_browser):
   page = MainPage_book(web_browser)
   page.sertificate.click()
   time.sleep(1)
def test_top_list(web_browser):
   page = MainPage_book(web_browser)
   page.top_list.click()
   time.sleep(1)
def test_news(web_browser):
   page = MainPage_book(web_browser)
   page.news.click()
   time.sleep(1)
def test_reductions(web_browser):
   page = MainPage_book(web_browser)
   page.reductions.click()
   time.sleep(1)

def test_phone(web_browser):
   page = MainPage_book(web_browser)
   page.phone.click()
   time.sleep(1)

def test_contact(web_browser):
   page = MainPage_book(web_browser)
   page.contact.click()
   time.sleep(1)
def test_support(web_browser):
   page = MainPage_book(web_browser)
   page.suport.click()
   time.sleep(1)


def test_station(web_browser):
   page = MainPage_book(web_browser)
   page.station.click()
   time.sleep(1)
# Работа часть 1.5 поменять свое решение
#Пошагово убедится, что работает
def test_change_page(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Гоголь'
   page.search_run_button.click()
   page.button.click()
   page.search_run_button_down = 'Пушкин'
   page.search_run_button_down.click()
#Пошагово убедится, что работает(более разнообразие ) !
def test_change_page_1(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Гоголь'
   page.search_run_button.click()
   page.button.click()
   page.search_run_button_down = 'Эдгар По'
   page.search_run_button_down.click()
   page.subject.right_mouse_click()
   #time.sleep(2)
   page.sort_table.click()
   all_prices = page.product_cost.get_text()
   all_prices = [float(p.replace(' ', '')) for p in all_prices]
   assert all_prices == sorted(all_prices)

def test_change_page_the_book_1(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Эдгар'
   page.search_run_button.click()
   page.button.click()
   page.cast_all.click()
   time.sleep(2)
   page.only_Russian.click()
def test_change_page_the_book_2(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Эдгар'
   page.search_run_button.click()
   page.type_producte.click()
   page.type_producte_paper_delete.click()
   time.sleep(2)
   page.OK.click()
   time.sleep(2)
def test_change_page_the_book_1(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.there_are.click()
   page.wait_delete.click()
   page.preoder_delete.click()
   page.mistake_delete.right_mouse_click()
   page.give.click()
   time.sleep(2)
def test_change_page_the_book_1(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.real_cost.click()
   page.from_cost.send_keys('100')
   page.until_cost.send_keys('2000')
   page.devilery_home.click()
   page.look.click()
   time.sleep(4)
def test_change_page_space(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.specify_place.click()
   time.sleep(4)
   page.specify_book.click()
   page.specify_all_book.click()
   time.sleep(4)
def test_change_page_space_1(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.specify_place.click()
   time.sleep(4)
   page.specify_book.click()
   page.specify_book_comic.click()
   page.specify_book_comic_all.click()
   time.sleep(4)
def test_change_page_space_2(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.specify_place.click()
   time.sleep(4)
   page.specify_book.click()
   time.sleep(2)
   page.specify_book_non_art.click()
   page.specify_book_non_art_all.click()
   time.sleep(2)

#Нужна немнго добваить время,а иначе не получится (очень важно!!!)!
def test_change_page_space_3(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.specify_place.click()
   time.sleep(4)
   page.specify_book.click()
   time.sleep(2)
   page.specify_book_idiom.click()
   page.specify_book_idiom_all.click()
   time.sleep(2)
def test_change_page_space_4(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.specify_place.click()
   time.sleep(4)
   page.specify_book.click()
   time.sleep(2)
   page.specify_book_ART.click()
   page.specify_book_ART_all.click()
   time.sleep(2)


#Нужна немнго добваить время,а иначе не получится (очень важно, не больше 2 сек !!!)!
def test_change_page_space_5(web_browser):
   page = MainPage_change_book(web_browser)
   page.search = 'Лавкрафт'
   page.search_run_button.click()
   page.specify_place.click()
   time.sleep(4)
   page.specify_audio.click()
   time.sleep(2)
   page.specify_audio_1.click()
   page.specify_audio_2.click()
   time.sleep(3)
#Немного о помощи  работа часть 1.6
def test_simple_eighteen_1(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.search_mylabirint.click()
    page.search_mylabirint_1.click()
    page.devilery_need.click()
    time.sleep(2)
def test_simple_eighteen_2(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.tax.click()
    page.pay.click()
    time.sleep(3)
def test_simple_eighteen_3(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.search_help.click()
    page.search_help_button.click()
def test_simple_eighteen_4(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.search_help='wdfehjwdfehhdjhidjwdjqdnkjwdwdjhki!!##$4'
    page.search_help_button.click()
def test_simple_eighteen_5(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.search_help='доставка'
    page.search_help_button.click()
#как оформить заказ долго грузит
def test_simple_eighteen_6(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.pay.click()
    page.how_ofform.click()
    time.sleep(1)
    page.how_ofform_1.click()
    time.sleep(8)
def test_simple_eighteen_7(web_browser):
    page=MainPage_help(web_browser)
    page.search_eighteen.click()
    time.sleep(2)
    page.tax.click()
    page.tax_1.click()
    time.sleep(1)
    page.tax_2.click()
    time.sleep(8)

