import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage_negative(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
    search = WebElement(id='search-field')
    search_run_button= WebElement(xpath='//*[@id="searchform"]/div[1]/button')
    search_written= WebElement(xpath='//*[@id="left"]/div[1]/form/div[1]/div/input')
    #обьявление для убежении! обычно проверяет почту
    searchreport=WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]')
    #сортируем как удобно
    sort_table = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[6]/span/a[2]')
    product_cost = ManyWebElements(xpath='//div[@product-pricing="price"]//span/*[1]')
    # ищем любого автора
    Author = WebElement(css_selector='#stab-slider-frame > ul > li:nth-child(2) > a')
    Try_bye=WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/table/tbody/tr[2]/td[5]/div/div/div[1]')
    Try_bye_check=WebElement(xpath='//*[@id="minwidth"]/div[6]/div[1]/div[1]/div[2]/div/ul/li[6]')

    button = WebElement(css_selector='#catalog-navigation > form > div.navisort-find.form-blue.putordergroup.col-xs-12 > div.text-cont.cleanable-search > span')
    search_run_button_down = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[3]/div[2]/input')
    subject = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[3]/div[1]')



    product_cost = ManyWebElements(xpath='//div[@product-pricing="price"]//span/*[1]')
