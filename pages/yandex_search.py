from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.ID, "search-result")
    LOCATOR_YANDEX_FIRST_RESULT = (By.LINK_TEXT, "tensor.ru")


class Search(BasePage):

    # Поиск поля для ввода запросов, ввод запроса
    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        # доп. время для отображения таблицы suggest
        time.sleep(5)
        return search_field

    # Нажатие на кнопку enter
    def key_enter(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)

    # Проверка на отображение поля для ввода запросов
    def search_field_is_displayed(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        return search_field.is_displayed()

    # Отображение suggest
    def suggest_is_displayed(self):
        suggest = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)
        return suggest.is_displayed()

    # Отображение результатов поиска
    def search_result_is_displayed(self):
        result = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULT)
        return result.is_displayed()

    # Проверка на соответствие 1 ссылки, адресу - tensor.ru
    def first_result(self):
        first = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_RESULT)
        URL = first.get_attribute("href")
        return "tensor.ru" in URL
        # другой вариант проверки:
        #if first == "tensor.ru":
        #    return first
        #else:
        #    return  first.is_displayed()

