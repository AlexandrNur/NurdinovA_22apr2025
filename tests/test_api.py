import pytest
from api.cart_api import CartAPI
import allure


@allure.feature('API Корзина')
class TestCartAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        """ Создание экземпляра API клиента для тестов. """
        self.cart_api = CartAPI()

    @allure.title("Добавление продукта в корзину")
    @allure.step("Тест добавления товара в корзину")
    def test_add_product_to_cart(self):
        """
        Проверяет успешное добавление продукта в корзину через API.
        """
        response = self.cart_api.add_product_to_cart()
        assert response.status_code == 200, f"Не удалось добавить продукт, статус код: {response.status_code}"

    @allure.title("Изменение количества товара")
    @allure.step("Тест изменения количества товара в корзине")
    def test_update_product_quantity(self):
        """
        Проверяет успешное обновление количества продукта в корзине через API.
        """
        response = self.cart_api.update_product_quantity()
        assert response.status_code == 200, f"Не удалось обновить количество, статус код: {response.status_code}"

    @allure.title("Получение содержимого корзины")
    @allure.step("Тест получения содержимого корзины")
    def test_get_cart_contents(self):
        """
        Проверяет успешное получение содержимого корзины через API.
        """
        response = self.cart_api.get_cart_contents()
        assert response.status_code == 200, f"Не удалось получить содержимое корзины, статус код: {response.status_code}"

    @allure.title("Удаление продукта из корзины")
    @allure.step("Тест удаления продукта из корзины")
    def test_remove_product_from_cart(self):
        """
        Проверяет успешное удаление продукта из корзины через API.
        """
        response = self.cart_api.remove_product_from_cart()
        assert response.status_code == 200, f"Не удалось удалить продукт, статус код: {response.status_code}"
