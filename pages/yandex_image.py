from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SERVICES =(By.LINK_TEXT, "Все")
    LOCATOR_YANDEX_IMAGES = (By.LINK_TEXT, "Картинки")
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.CLASS_NAME , "PopularRequestList-SearchText")
    LOCATOR_YANDEX_IMAGE_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_YANDEX_FIRST_PIC = (By.CLASS_NAME, "serp-item")
    LOCATOR_YANDEX_FIRST_PIC_DISPL = (By.CLASS_NAME, "MMImage-Preview")
    LOCATOR_YANDEX_NEXT_PIC = (By.CLASS_NAME, "CircleButton_type_next ")
    LOCATOR_YANDEX_PREVIOUS_PIC = (By.CLASS_NAME, "CircleButton_type_prev ")


class Images(BasePage):

    # Поиск кнопки меню
    def services_is_displayed (self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        # доп. время для отображения таблицы suggest и кнопки со всеми сервисами
        time.sleep(5)
        services = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SERVICES)
        return services.is_displayed()

    # Нажатие на кнопку меню
    def menu(self):
        menu_of_services = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SERVICES)
        menu_of_services.click()
        time.sleep(5)

    # Нажатие на кнопку 'Картинки'
    def img(self):
        menu_img = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES)
        menu_img.click()
        time.sleep(5)

    # Проверка на соответвие адреса
    def check_url(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        checkURL = self.driver.current_url
        #print(checkURL)
        #is_it_change = WebDriverWait(self, 10).until(EC.url_to_be("https://ya.ru/images/"))
        return checkURL

    # Переход на первую категорию в разделе "Картинки"
    def first_category_image(self):
        first_category = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY)
        first_category.click()
        time.sleep(5)

    #def category_name(self):
    #    c_name = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY)
    #    pc=c_name.get_attribute("value")
    #    return pc

    # Отображение названия картинки в поле поисковой системы
    def name_of_category_is_displayed(self):
        name_of_category = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGE_SEARCH_FIELD)
        category_name = bool(name_of_category.get_attribute("value"))
        time.sleep(5)
        return category_name

    # Функция, открывающая 1 картинку в выбранной категории
    def pic(self):
        picture = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_PIC)
        picture.click()
        time.sleep(5)

    # Отображение картинки
    def pic_is_displayed(self):
        picture_isDispl = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_PIC_DISPL)
        return picture_isDispl.is_displayed()

    # Получаем текущий адрес картинки для дальнейшего сравнения при переключении картинок
    def current_pic(self):
        pic_text = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_PIC_DISPL)
        return pic_text.get_attribute("src")

    # Нажатие кнопки вперед (следующая картинка)
    def next_pic(self):
        next_picture = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NEXT_PIC)
        next_picture.click()
        time.sleep(5)

    # Нажатие кнопки назад (предыдущая картинка)
    def previous_pic(self):
        prev_pic = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PREVIOUS_PIC)
        prev_pic.click()
        time.sleep(5)
