import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    search = WebElement(id='search-field')
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button')
    search_eighteen=WebElement(css_selector='#minwidth > div.top-header > div.b-header-outer > div.b-header > a')


class MainPage_story(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
    search = WebElement(id='search-field')

    # Search button
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button')
    search_book_bye_1 = WebElement(xpath= '//*[@id="buy777176"]')
    search_book_bye_2 = WebElement(css_selector='#buy771545' )
    search_book_check = WebElement(xpath='/html/body/div[1]/div[5]/div[6]/div[1]/div[1]/div[2]/div/ul/li[6]/a')
class MainPage_time(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
    book = WebElement(css_selector='#minwidth > div.top-header > div.b-header-outer > div.b-header > div.b-header-b-menu.col-xs-12.col-sm-12.col-md-10.js-toggle-menu-block > div > div.js-b-header-b-menu-e-slider > ul > li:nth-child(1) > span')
    search_popular= WebElement(xpath='//*[@id="header-genres"]/div/ul/li[2]')

    search_popular_all = WebElement(xpath = ' //*[@id="header-genres"]/div/ul/li[3]')
class MainPage_cost(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='search-field')

    # Search button
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button')
    sort_table= WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[6]/span/a[2]')
    #Другя страница - это важно!
    sort_table_1=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[4]/span/a[2]')
    #product_cost = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
    product_cost = ManyWebElements(xpath='//div[@product-pricing="price"]//span/*[1]')
    #ищем любого автора
    Author = WebElement(css_selector='#stab-slider-frame > ul > li:nth-child(2) > a')
    #Например Лермотов
    Authour_Lermotov = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[5]')
    #Акции
    deal=WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[3]')
    #Обзоры
    reviews=WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[4]/a')
    #видео
    video=WebElement(css_selector='#stab-slider-frame > ul > li.b-stab-e-slider-item.active.b-stab-e-slider-item-m-active > a')
    #Новости
    newspaper=WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[6]/a')
class MainPage_book(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    search = WebElement(id='search-field')
    book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[1]')
    #под search
    number_one= WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[2]')
    school= WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[3]')
    playgame= WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[4]')
    club = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[11]')
    place=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[1]')
    develery=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[2]')
    #под меню
    cost_pay=WebElement(css_selector='#minwidth > div.top-header > div.b-header-outer > div.b-header-b-sec-menu.col-md-12 > div > ul > li.b-header-b-sec-menu-e-list-item.first-child.analytics-click-js')
    sertificate=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[2]')
    top_list=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[3]')
    news=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[4]')
    reductions=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[5]')
    phone=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[6]')
    contact=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[9]')
    suport=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[10]')
    station=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[11]')

class MainPage_change_book(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
    # Main search field
    search = WebElement(id='search-field')

    # change
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button')
    button=WebElement(css_selector='#catalog-navigation > form > div.navisort-find.form-blue.putordergroup.col-xs-12 > div.text-cont.cleanable-search > span')
    search_run_button_down=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[3]/div[2]/input')
    subject=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[3]/div[1]')

    sort_table = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[6]/span/a[2]')

    product_cost = ManyWebElements(xpath='//div[@product-pricing="price"]//span/*[1]')
    #Тип продукта
    cast_all= WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[2]/div/div/span[2]')
    only_Russian= WebElement(css_selector='#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div.swiper-container-navisort.swiper-container-navisort-reset.swiper-container-initialized.swiper-container-horizontal.swiper-container-free-mode > div > div > span:nth-child(3) > label')

    type_producte=WebElement(css_selector='#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-filter.navisort-part-1.fleft')
    type_producte_paper_delete=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[2]/ul/li[1]')
    OK=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[2]/ul/li[5]')
    #Наличие
    there_are=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]/span')
    wait_delete=WebElement(css_selector='#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-filter.navisort-part-2.fleft > span > span > span.menu-items > ul > li:nth-child(3)')
    preoder_delete=WebElement(css_selector='#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-filter.navisort-part-2.fleft > span > span > span.menu-items > ul > li:nth-child(2)')
    mistake_delete=WebElement(css_selector='#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-filter.navisort-part-2.fleft > span > span > span.menu-items > ul > li:nth-child(1)')
    give=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]/span/span/span[2]/ul/li[6]')
    #цена
    real_cost=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[1]')
    from_cost=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[2]/ul/li[1]/label/input[1]')
    until_cost=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[2]/ul/li[1]/label/input[2]')
    devilery_home=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[2]/ul/li[3]')
    look=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[2]/ul/li[5]')
    #Уточнить место
    specify_place=WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[4]/span')
    specify_book = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]')
    specify_book_comic=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[3]')
    specify_book_comic_all=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[3]/div[2]/ul/li[1]/a')

    specify_all_book =WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[1]')
    specify_book_non_art=WebElement(xpath ='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[4]/div[1]')
    specify_book_non_art_all=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[4]/div[2]/ul/li[1]/a')

    specify_book_idiom=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[5]')
    specify_book_idiom_all=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[5]/div[2]/ul/li[1]')

    specify_book_ART=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[6]/div[1]')
    specify_book_ART_all=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[2]/div[2]/ul/li[6]/div[2]/ul/li[1]')

    specify_audio=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[1]/div[1]')
    specify_audio_1=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[1]/div[2]/ul/li')
    specify_audio_2=WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[2]/div/div/div[3]/div[2]/ul/li[1]/div[2]/ul/li/div[2]/ul/li')
class MainPage_help(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
    # Main search field
    search = WebElement(id='search-field')
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button')
    search_eighteen = WebElement(css_selector='#minwidth > div.top-header > div.b-header-outer > div.b-header > a')
    search_mylabirint=WebElement(id='aHelp')
    search_mylabirint_1=WebElement(xpath='//*[@id="right-inner"]/div/div[1]/div/div[1]/img')
    #доставка
    devilery_need=WebElement(xpath='//*[@id="right-inner"]/div/div[1]/div/div[3]')
    #Скидки
    tax=WebElement(xpath='//*[@id="right-inner"]/div/div[1]/div/div[5]/img')
    tax_1=WebElement(xpath='//*[@id="helpmenu3"]/div[1]')
    tax_2=WebElement(xpath='//*[@id="tdcard103"]/div/div[1]/span')
    #оплата
    pay=WebElement(xpath='//*[@id="right-inner"]/div/div[1]/div/div[7]/img')
    how_ofform=WebElement(xpath='//*[@id="right-inner"]/div/div[1]/div/div[9]')
    how_ofform_1=WebElement(xpath='//*[@id="tdcard192"]/div/div[1]/span')

    search_help=WebElement(id='txtwordsadv')
    search_help_button=WebElement(xpath='//*[@id="right-inner"]/div/div[2]/div[1]/div/form/div[2]/input[2]')