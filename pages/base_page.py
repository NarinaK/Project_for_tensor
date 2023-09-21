from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https:/ya.ru/"


    # Поиск элементов
    def find_element (self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    # Переход на заданный url
    def go_to_site(self):
        return self.driver.get(self.base_url)


    # Обновление страницы
    def refresh(self):
        logging.info("Страница обновлена")
        return self.driver.refresh()
