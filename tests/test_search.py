from pages.yandex_search import Search
import logging


def test_search(browser):
    yandex_main_page = Search(browser)

    logging.basicConfig(level=logging.INFO, filename="py_log_search.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # 1. Переход на сайт https://ya.ru/
    yandex_main_page.go_to_site()
    logging.info("Открыта страница https:/ya.ru/")

    # 2. Проверка наличия поля поиска
    assert yandex_main_page.search_field_is_displayed(), "Нет поля поиска"
    logging.info("Поле поиска отображается")

    # 3. Ввод в поле поиска слово "Тензор"
    yandex_main_page.enter_word("Тензор")
    logging.info("Введено слово 'Тензор' в поле поиска")

    # 4. Проверка на наличие таблицы с подсказками (suggest)
    assert yandex_main_page.suggest_is_displayed(), "Таблица с подсказками (suggest) не отображается"
    logging.info("Таблица с подсказками (suggest) отображается")

    # 5. Нажатие кнопки Enter
    yandex_main_page.key_enter()
    logging.info("Нажата клавиша Enter")

    # 6. Проверка наличия/отображения результатов поиска
    assert yandex_main_page.search_result_is_displayed(), "На странице не отображаются результаты поиска"
    logging.info("Страница результатов поиска отображается")

    # 7. Проверка на соответствие 1 ссылки url адресу tensor.ru
    assert yandex_main_page.first_result(), "Первая ссылка ведет не на сайт tensor.ru"
    logging.info("Первая ссылка ведет на сайт tensor.ru")