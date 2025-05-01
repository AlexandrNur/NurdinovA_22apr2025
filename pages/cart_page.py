from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class CartPage(BasePage):
    """
    Страница корзины для работы с элементами и действиями внутри корзины.
    """

    @allure.step("Переход в корзину")
    def navigate_to_cart(self):
        """
        Открывает страницу корзины.
        """
        cart_mini = self.wait_for(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.header__basket-link'))
        )
        cart_mini.click()

    @allure.step("Получение количества первого товара в корзине")
    def get_first_product_quantity(self):
        """
        Возвращает количество первого продукта в корзине.

        :return: количество первого продукта.
        """
        initial_quantity_element = self.wait_for(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.num'))
        )
        return int(initial_quantity_element.text)

    @allure.step("Увеличение количества первого товара в корзине")
    def increase_first_product_quantity(self):
        """
        Увеличивает количество первого продукта в корзине на 1.
        """
        increase_button = self.wait_for(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.more.js-plus'))
        )
        increase_button.click()
