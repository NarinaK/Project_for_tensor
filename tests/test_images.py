from pages.yandex_image import Images
import logging


def test_img(browser):
    yandex_main_page = Images(browser)

    logging.basicConfig(level=logging.INFO, filename="py_log_images.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # 1. Переход на сайт https://ya.ru/
    yandex_main_page.go_to_site()
    logging.info("Открыта страница https:/ya.ru/")

    # 2. Проверить, что кнопка меню присутствует на странице
    assert yandex_main_page.services_is_displayed(), "Нет кнопки меню"
    logging.info("Кнопка меню отображается на странице")

    # 3. Открыть меню, выбрать "Картинки"
    yandex_main_page.menu()
    logging.info("Нажата кнопка меню")
    yandex_main_page.img()
    logging.info("Нажата кнопка 'Картинки'")

    # 4. Проверить, что перешли на url https://ya.ru/images/
    assert yandex_main_page.check_url() == "https://ya.ru/images/", "Переход на страницу https://ya.ru/images/ не осуществлен"
    logging.info("Переход на страницу https://ya.ru/images/")
    #current_name = yandex_main_page.category_name()

    # 5. Открыть первую категорию
    yandex_main_page.first_category_image()
    logging.info("Открыта первая категория в разделе популярных изображений")

    # 6. Проверить, что название категории отображается в поле поиска
    # yandex_main_page.refresh()
    assert yandex_main_page.name_of_category_is_displayed(),"Название категории не отображается в поле поиска"
    logging.info("Название категории отображено в поле поиска")

    # 7. Открыть 1 картинку
    yandex_main_page.pic()
    logging.info("Выбрана 1 картинка в разделе")

    # 8. Проверить, что картинка открылась
    assert yandex_main_page.pic_is_displayed(), "Картинка не открылась"
    pic_name = yandex_main_page.current_pic()
    logging.info("Картинка открылась")

    # 9. Нажать кнопку вперед
    yandex_main_page.next_pic()
    logging.info("Нажата кнопка вперед")

    # 10. Проверить, что картинка сменилась
    assert pic_name != yandex_main_page.current_pic(), "Картинка не сменилась"
    logging.info("Картинка сменилась на следующую")

    # 11. Нажать назад
    yandex_main_page.previous_pic()
    logging.info("Нажата кнопка назад")

    # 12. Проверить, что картинка осталась из шага 8
    assert yandex_main_page.current_pic() == pic_name, "Отобразилась не предыдущая картинка"
    logging.info("Картинка сменилась на изначальную (из шага 8)")