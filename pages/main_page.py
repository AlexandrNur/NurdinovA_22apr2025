from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
import config
import allure


class MainPage(BasePage):
    """
    Страница главного раздела пользовательского интерфейса.
    """

    @allure.step("Навигация к главной странице")
    def navigate_to(self):
        """
        Переходит на главную страницу сайта.
        """
        self.driver.get(config.BASE_URL_UI)

    @allure.step("Открытие категории продуктов")
    def open_product_category(self):
        """
        Открывает категорию продуктов на главной странице.
        """
        product_search = self.wait_for(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/tag/joints/"]'))
        )
        product_search.click()

    @allure.step("Добавление товаров в корзину (макс. {max_items} товаров)")
    def add_products_to_cart(self, max_items=4):
        """
        Добавляет указанные товары в корзину.

        :param max_items: максимальное количество товаров для добавления.
        :return: фактическое количество добавленных товаров.
        """
        elements = self.wait_for(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product__add_2_0'))
        )
        num_items_to_add = min(max_items, len(elements))
        for element in elements[:num_items_to_add]:
            button = element.find_element(By.TAG_NAME, 'button')
            button.click()
        return num_items_to_add

    @allure.step("Проверка количества товаров в корзине (ожидалось: {expected_count})")
    def check_cart_quantity(self, expected_count):
        """
        Проверяет, что количество товаров в корзине соответствует ожидаемому значению.

        :param expected_count: ожидаемое количество товаров в корзине.
        """
        items_in_cart = self.wait_for(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.count.js-count-number.active'))
        )
        cart_count = int(items_in_cart.text)
        assert cart_count == expected_count, (
            f"Ошибка: число добавленных ({expected_count}) не соответствует количеству в корзине ({cart_count})."
        )
