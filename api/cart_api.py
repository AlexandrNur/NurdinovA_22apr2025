import requests
from config import (
    BASE_URL_API,
    add_product_data,
    update_quantity_data,
    get_cart_contents_data,
    remove_product_data
)


class CartAPI:
    """
    Класс для работы с API корзины.
    """
    def __init__(self):
        self.base_url = BASE_URL_API

    def add_product_to_cart(self):
        """
        Добавляет продукт в корзину.

        :return: ответ сервера.
        """
        url = f"{self.base_url}/cart/add_products_to_cart_from_preview.php"
        response = requests.post(url, data=add_product_data)
        return response

    def update_product_quantity(self):
        """
        Обновляет количество продукта в корзине.

        :return: ответ сервера.
        """
        url = f"{self.base_url}/cart/action_with_basket_on_cart_page.php"
        response = requests.post(url, data=update_quantity_data)
        return response

    def get_cart_contents(self):
        """
        Получает содержимое корзины.

        :return: ответ сервера.
        """
        url = f"{self.base_url}/ajax/ajax_ecommerce/ajax_ecommerce.php"
        response = requests.post(url, data=get_cart_contents_data)
        return response

    def remove_product_from_cart(self):
        """
        Удаляет продукт из корзины.

        :return: ответ сервера.
        """
        url = f"{self.base_url}/cart/delete_products_from_cart_preview.php"
        response = requests.post(url, data=remove_product_data)
        return response
