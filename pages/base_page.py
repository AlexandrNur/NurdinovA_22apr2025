from selenium.webdriver.support.ui import WebDriverWait
import allure


class BasePage:
    """
    Базовый класс для всех страниц. Содержит общие методы работы с веб-элементами.
    """
    def __init__(self, driver):
        """
        Инициализация базовой страницы с веб-драйвером.
        """
        self.driver = driver

    @allure.step("Ожидание условия в течение {timeout} секунд")
    def wait_for(self, condition, timeout=10):
        """
        Ожидание выполнения условия на странице.

        :param condition: условие, которое необходимо ожидать.
        :param timeout: количество секунд ожидания.
        :return: элемент, удовлетворяющий условию.
        """
        return WebDriverWait(self.driver, timeout).until(condition)
