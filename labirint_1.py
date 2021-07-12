import os


from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
class MainPage_down(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
    overlap= ManyWebElements(xpath='//div[@class="body-top"]/div[5]/div[2]/div/div[1]/div[1]/div[2]/a[1]')
    apple= WebElement(xpath = '//*[@id="body-top"]/div[6]/div[2]/div/div[1]/div[1]/div[2]/a[1]')
    google=WebElement(xpath='//*[@id="body-top"]/div[6]/div[2]/div/div[1]/div[1]/div[2]/a[2]')
    apple_gallery=WebElement(xpath='//*[@id="body-top"]/div[6]/div[2]/div/div[1]/div[1]/div[2]/a[3]')