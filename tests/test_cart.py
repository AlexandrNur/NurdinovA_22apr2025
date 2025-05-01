import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.cart_page import CartPage
import allure


@pytest.fixture(scope="function")
def setup():
    """
    Фикстура для настройки и завершения сеанса веб-драйвера.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.feature('Корзина')
@allure.story('Добавление товара в корзину')
def test_add_product_to_cart(setup):
    """
    Тест проверяет добавление товара в корзину и сравнивает количество.
    """
    driver = setup
    main_page = MainPage(driver)

    with allure.step("Переход на главную страницу и открытие категории продуктов"):
        main_page.navigate_to()
        main_page.open_product_category()

    with allure.step("Добавление товаров в корзину и проверка количества"):
        num_items_to_add = main_page.add_products_to_cart()
        main_page.check_cart_quantity(num_items_to_add)


@allure.feature('Корзина')
@allure.story('Изменение количества товаров в корзине')
def test_increase_product_quantity(setup):
    """
    Тест проверяет увеличение количества товара в корзине.
    """
    driver = setup
    main_page = MainPage(driver)
    cart_page = CartPage(driver)

    with allure.step("Переход на главную страницу, открытие категории и добавление товаров в корзину"):
        main_page.navigate_to()
        main_page.open_product_category()
        main_page.add_products_to_cart()

    with allure.step("Перейти к корзине"):
        cart_page.navigate_to_cart()

    with allure.step("Увеличить количество первого товара в корзине"):
        initial_quantity = cart_page.get_first_product_quantity()
        cart_page.increase_first_product_quantity()
        updated_quantity = cart_page.get_first_product_quantity()

        assert updated_quantity == initial_quantity + 1, (
            f"Ошибка: количество товара не увеличилось правильно. Ожидалось {initial_quantity + 1}, получено {updated_quantity}."
        )
